import unittest
from task import *
from matplotlib.colors import ListedColormap
from unittest.mock import patch



# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    filename = '/Users/kamalia/PycharmProjects/Charts with matplotlib/StepByStepProject/Project/dataset.csv'
    df = pd.read_csv(filename)
    def test_required_columns(self):
        result = required_columns(df)
        pd.testing.assert_frame_equal(result, df[['name', 'platform', 'genre']])
    def test_interested_platforms(self):
        result = required_columns(df)
        final_result = interested_platforms(result)
        platforms_of_interest = ['PS4', 'XOne', 'PC', 'WiiU']
        result['platform'] = pd.Categorical(result['platform'], categories=platforms_of_interest, ordered=True)
        df_filtered = result[result['platform'].isin(platforms_of_interest)]
        pd.testing.assert_frame_equal(final_result, df_filtered)

    def test_group_data(self):
        filtered_df = interested_platforms(required_columns(df))
        result = group_data(filtered_df)
        grouped_data = filtered_df.groupby(['platform', 'genre'], observed=False).size().unstack(fill_value=0)
        pd.testing.assert_frame_equal(result,grouped_data)

    def test_bar_chart_details(self):
        grouped_data = group_data(interested_platforms(required_columns(df)))
        result_bar_width, result_x, result_platforms, result_genres, result_colors = bar_chart_details(grouped_data)
        bar_width = 0.2
        self.assertEqual(result_bar_width, bar_width, "Бар ширины не совпадает с ожидаемым значением")

        # Определяем количество платформ и позиции для них на оси x
        x = np.arange(len(grouped_data.index))  # Positions for platforms
        self.assertTrue(np.array_equal(result_x, x), "Массив позиций для платформ не совпадает с ожидаемым")

        platforms = grouped_data.index
        self.assertTrue(np.array_equal(result_platforms, platforms), "Список платформ не совпадает с ожидаемым")

        genres = grouped_data.columns
        self.assertTrue(np.array_equal(result_genres, genres), "Список жанров не совпадает с ожидаемым")

        colors = plt.get_cmap('tab20', len(genres))  # Используем палитру 'tab20'
        self.assertIsInstance(result_colors, ListedColormap, "Тип палитры должен быть ListedColormap")
        self.assertEqual(result_colors.N, colors.N,
                         "Количество цветов в палитре не совпадает с количеством жанров")

    def test_set_positions(self):
        # Подготовка данных для вызова функции
        filtered_df = interested_platforms(required_columns(self.df.copy()))
        grouped_df = group_data(filtered_df)
        bar_width, x, platforms, genres, colors = bar_chart_details(grouped_df)

        # Вызов функции
        x_positions = set_positions(bar_width, platforms, genres, colors, grouped_df)

        # Тест 1: Проверка корректности позиций на оси x
        expected_x_positions = np.arange(len(platforms)) * (bar_width * len(genres) + 0.1)
        np.testing.assert_array_almost_equal(x_positions, expected_x_positions,
                                             err_msg="Позиции на оси X не совпадают с ожидаемыми")

        # Тест 2: Проверка количества столбцов для каждого жанра
        fig = plt.figure()
        set_positions(bar_width, platforms, genres, colors, grouped_df)
        ax = fig.gca()

        tolerance = 0.05 * bar_width  # Допуск ±5% от ширины бара
        bars = [
            bar for bar in ax.get_children()
            if isinstance(bar, plt.Rectangle) and bar.get_height() >= 0
               and (bar_width - tolerance) <= bar.get_width() <= (bar_width + tolerance)
        ]
        expected_bar_count = len(platforms) * len(genres)

        self.assertEqual(len(bars), expected_bar_count, "Количество столбцов на графике не совпадает с ожидаемым")

        # Тест 3: Проверка цвета для каждого жанра, игнорируя альфа-канал
        for i, genre in enumerate(genres):
            expected_color = colors(i)[:3]  # Только RGB, без альфа-канала
            for bar in bars[i*len(platforms): (i+1)*len(platforms)]:
                actual_color = bar.get_facecolor()[:3]  # Только RGB, без альфа-канала
                self.assertEqual(actual_color, expected_color,
                                 f"Цвет столбца для жанра {genre} не совпадает с ожидаемым")

        plt.close(fig)  # Закрываем график после тестирования


