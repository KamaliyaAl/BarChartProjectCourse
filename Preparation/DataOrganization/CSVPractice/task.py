import pandas as pd

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df

def display_first_n_rows(df, n):
    return df.head(n)

def drop_missing_values(df):
    df_cleaned = df.dropna()
    return df_cleaned

file_path = 'employees.csv'

df = read_csv_file(file_path)

first_seven_rows = display_first_n_rows(df, 7)
print("First 7 rows:")
print(first_seven_rows)

df_cleaned = drop_missing_values(df)
