import unittest
from Preparation.DataOrganization.CSVPractice.task import *


# todo: replace this with an actual test
class TestCase(unittest.TestCase):

    def setUp(self):
        # Путь к файлу для тестирования
        self.csv_file_path = 'employees.csv'
        self.df = pd.read_csv(self.csv_file_path)

    def test_read_csv_file(self):
        df = pd.read_csv(self.csv_file_path)
        pd.testing.assert_frame_equal(df, read_csv_file(
            self.csv_file_path))

    def test_display_first_n_rows(self):
        first_7_rows_expected = self.df.head(7)
        first_7_rows_result = display_first_n_rows(self.df, 7)
        pd.testing.assert_frame_equal(first_7_rows_expected, first_7_rows_result)  # Сравнение двух DataFrame

    def test_drop_missing_values(self):
        df_cleaned_expected = self.df.dropna()
        df_cleaned_result = drop_missing_values(self.df)
        pd.testing.assert_frame_equal(df_cleaned_expected, df_cleaned_result)  # Сравнение DataFrame после удаления NaN



