import unittest
from Preparation.IntroductionToPandasLibrary.SeriesManipulations.task import *


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_create_series(self):
        list = [5, 15, 25, 35, 45, 55, 65]
        indexes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        pd.testing.assert_series_equal(create_series(list, indexes), pd.Series(list, index = indexes)['b':'e'])

    def test_multiply_salary(self):
        list = [5, 15, 25, 35, 45, 55, 65]
        indexes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        series = create_series(list, indexes)
        pd.testing.assert_series_equal(multiply_series(series), series*2)

    def test_filter_salary(self):
        list = [5, 15, 25, 35, 45, 55, 65]
        indexes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        series = create_series(list, indexes)
        pd.testing.assert_series_equal(filter_series(series), series[series>50])

