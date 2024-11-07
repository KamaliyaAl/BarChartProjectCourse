import unittest
from task import *


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def setUp(self):
        self.filename = '/Users/kamalia/PycharmProjects/Charts with matplotlib/StepByStepProject/Project/dataset.csv'

    def test_load_the_data(self):
        # Вызов тестируемой функции
        result = load_the_data(self.filename)
        # Проверка, что результат совпадает с ожидаемым DataFrame
        pd.testing.assert_frame_equal(result, pd.read_csv(
            '/Users/kamalia/PycharmProjects/Charts with matplotlib/StepByStepProject/Project/dataset.csv'))