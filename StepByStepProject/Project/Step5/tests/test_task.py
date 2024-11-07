import unittest
from task import *
from matplotlib.colors import ListedColormap



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
        self.assertEqual(result_bar_width, bar_width, "Bar width is not 0.2")

        # Определяем количество платформ и позиции для них на оси x
        x = np.arange(len(grouped_data.index))  # Positions for platforms
        self.assertTrue(np.array_equal(result_x, x), "Massive with x-positions does not match the expected")

        platforms = grouped_data.index
        self.assertTrue(np.array_equal(result_platforms, platforms), "Platforms are not as required")

        genres = grouped_data.columns
        self.assertTrue(np.array_equal(result_genres, genres), "Genres are not as required")

        colors = plt.get_cmap('tab20', len(genres))
        self.assertIsInstance(result_colors, ListedColormap, "Not required colormap")
        self.assertEqual(result_colors.N, colors.N,
                         "Not the required number of colors")


