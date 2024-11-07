import unittest
import pandas as pd
from Preparation.IntroductionToPandasLibrary.DataFrameManipulations.task import *
from pandas.testing import assert_frame_equal

# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    data = {
        'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor'],
        'Price': [1000, 300, 500, 200],
        'Stock': [50, 100, 200, 150]
    }

    def test_create_df(self):
        # Ожидаемый DataFrame
        expected_df = pd.DataFrame(data)
        # Проверяем, что DataFrame создан корректно
        result_df = create_df(data)
        assert_frame_equal(result_df, expected_df)

    def test_select_columns(self):
        # Исходный DataFrame
        df = create_df(data)
        # Ожидаемый результат после выбора столбцов
        expected_df = pd.DataFrame({
            'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor'],
            'Price': [1000, 300, 500, 200]
        })
        # Проверяем выбор столбцов
        result_df = select_columns(df, ['Product', 'Price'])
        assert_frame_equal(result_df, expected_df)

    def test_add_column(self):
        # Исходный DataFrame
        df = pd.DataFrame(data)
        # Ожидаемый DataFrame с добавленным столбцом
        expected_df = pd.DataFrame({
            'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor'],
            'Price': [1000, 300, 500, 200],
            'Stock': [50, 100, 200, 150],
            'Total Value': [50000, 30000, 100000, 30000]
        })
        # Применяем добавление столбца и проверяем результат
        result_df = add_column(df).reset_index(drop=True)
        assert_frame_equal(result_df, expected_df)
