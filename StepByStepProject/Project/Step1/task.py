import pandas as pd

# Step 1: LoadTheData
def load_the_data(filename):
    df = pd.read_csv(filename)
    return df

# TODO
filename = ''
df = load_the_data(filename)

# Optional: Explore the loaded data: use the method df.head()
print(df.head())
