import unittest
from task import *


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def setUp(self):
        self.filename = '/Users/kamalia/PycharmProjects/Charts with matplotlib/StepByStepProject/Project/dataset.csv'
        self.df = pd.read_csv(self.filename)
    def test_required_columns(self):
        result = required_columns(self.df)
        pd.testing.assert_frame_equal(result, self.df[['name', 'platform', 'genre']])
    def test_interested_platforms(self):
        result = required_columns(self.df)
        final_result = interested_platforms(result)
        platforms_of_interest = ['PS4', 'XOne', 'PC', 'WiiU']
        result['platform'] = pd.Categorical(result['platform'], categories=platforms_of_interest, ordered=True)
        df_filtered = result[result['platform'].isin(platforms_of_interest)]
        pd.testing.assert_frame_equal(final_result, df_filtered)

