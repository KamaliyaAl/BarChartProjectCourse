import unittest
from matplotlib.testing.decorators import cleanup
import matplotlib.pyplot as plt
from Preparation.BasicConstruction.BarChart.task import *
class TestMatplotlibFunctions(unittest.TestCase):

    def test_define_data(self):
        categories, values = define_data()
        self.assertEqual(categories, ['A', 'B', 'C', 'D'])
        self.assertEqual(values, [25, 40, 35, 20])

    @cleanup
    def test_create_bar_chart_vertical(self):
        categories, values = define_data()
        create_bar_chart(categories, values, width=0.6, color='blue', orientation='vertical')
        ax = plt.gca()
        bars = ax.patches
        self.assertEqual(len(bars), 4)  # Убедимся, что 4 столбца нарисованы
        self.assertEqual(bars[0].get_width(), 0.6)  # Проверим ширину столбца

    @cleanup
    def test_create_bar_chart_horizontal(self):
        categories, values = define_data()
        create_bar_chart(categories, values, width=0.6, color='red', orientation='horizontal')
        ax = plt.gca()
        bars = ax.patches
        self.assertEqual(len(bars), 4)  # Убедимся, что 4 горизонтальных столбца нарисованы
        self.assertEqual(bars[0].get_height(), 0.6)  # Проверим высоту горизонтального столбца

    @cleanup
    def test_add_labels_and_title(self):
        add_labels_and_title('Categories', 'Values', 'Test Chart')
        ax = plt.gca()
        self.assertEqual(ax.get_xlabel(), 'Categories')
        self.assertEqual(ax.get_ylabel(), 'Values')
        self.assertEqual(ax.get_title(), 'Test Chart')

if __name__ == '__main__':
    unittest.main()
