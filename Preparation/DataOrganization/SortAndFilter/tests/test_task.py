import unittest
from Preparation.DataOrganization.SortAndFilter.task import *
class TestPandasFunctions(unittest.TestCase):

    def setUp(self):
        # Данные для тестов
        self.data = {
            'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Keyboard'],
            'Price': [1200, 350, 800, 250, 100],
            'Stock': [50, 100, 200, 150, 500]
        }
        self.df = pd.DataFrame(self.data)

    # Тест для сортировки
    def test_sort_by_stock_and_price(self):
        sorted_df = sort_by_stock_and_price(self.df)
        expected_result = ['Laptop', 'Tablet', 'Monitor', 'Smartphone', 'Keyboard']
        self.assertEqual(list(sorted_df['Product']), expected_result)

    # Тест для фильтрации по Stock и Price
    def test_filter_by_stock_and_price(self):
        filtered_df = filter_by_stock_and_price(self.df)
        expected_result = ['Smartphone', 'Monitor', 'Keyboard']
        self.assertEqual(list(filtered_df['Product']), expected_result)

    # Тест для фильтрации по названию продукта
    def test_filter_by_product_name(self):
        filtered_df = filter_by_product_name(self.df)
        expected_result = ['Smartphone']
        self.assertEqual(list(filtered_df['Product']), expected_result)

if __name__ == '__main__':
    unittest.main()
