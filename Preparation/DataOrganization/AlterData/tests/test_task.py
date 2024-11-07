import unittest
from Preparation.DataOrganization.AlterData.task import *
class TestPandasFunctions(unittest.TestCase):

    def setUp(self):
        self.data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Age': [25, None, 35, None, 45],
            'Salary': [50000, 60000, 70000, 80000, None]
        }
        self.df = pd.DataFrame(self.data)

    def test_rename_columns(self):
        renamed_df = rename_columns(self.df.copy())
        self.assertIn('Employee Name', renamed_df.columns)
        self.assertIn('Annual Salary', renamed_df.columns)

    def test_drop_missing_salary(self):
        filled_df = rename_columns(self.df.copy())
        dropped_df = drop_missing_salary(filled_df.copy())
        self.assertNotIn(None, dropped_df['Annual Salary'].values)

    def test_group_by_age_group(self):
        df_renamed = rename_columns(self.df.copy())
        df_dropped = drop_missing_salary(df_renamed.copy())
        expected_df = pd.DataFrame({
            'Age': [25.0, 35.0],
            'Annual Salary': [50000.0, 70000.0]
        })
        grouped_df = group_by_age_group(df_dropped.copy())
        pd.testing.assert_frame_equal(grouped_df.reset_index(drop=True), expected_df.reset_index(drop=True))

if __name__ == '__main__':
    unittest.main()
