import pandas as pd

def load_the_data(filename):
    df = pd.read_csv(filename)
    return df

filename = '/Users/kamalia/PycharmProjects/Charts with matplotlib/StepByStepProject/Project/dataset.csv'

# Step2: Inspect the dataset
def required_columns(df):
    df_required = df[['name', 'platform', 'genre']]
    return df_required


df = load_the_data(filename)
df = required_columns(df.copy())

# Optional: Explore the loaded data: print the methods df.head() and df.info()
print(df.head())
print(df.info())
