import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, None, 35, None, 45],
    'Salary': [50000, 60000, 70000, 80000, None]
}
df = pd.DataFrame(data)

def rename_columns(df):
    return df.rename(columns={'Name': 'Employee Name', 'Salary': 'Annual Salary'})

def drop_missing_salary(df):
    return df.dropna(subset=['Annual Salary'])

def group_by_age_group(df):
    return df.groupby('Age')['Annual Salary'].mean().reset_index()


df_renamed = rename_columns(df.copy())
df_dropped = drop_missing_salary(df_renamed.copy())
df_grouped = group_by_age_group(df_dropped.copy())

print("DataFrame after renaming:\n", df_renamed)
print("\nDataFrame after dropping rows with missing salary:\n", df_dropped)
print("\nMean salary by age group:\n", df_grouped)
