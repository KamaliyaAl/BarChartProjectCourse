import unittest
from task import *


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    filename = '/Users/kamalia/PycharmProjects/Charts with matplotlib/StepByStepProject/Project/dataset.csv'
    df = pd.read_csv(filename)
    def test_required_columns(self):
        result = required_columns(df)
        pd.testing.assert_frame_equal(result, df[['name', 'platform', 'genre']])
