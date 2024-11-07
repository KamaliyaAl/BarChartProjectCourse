import unittest
from task import *


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

