import pandas as pd

def load_the_data(filename):
    df = pd.read_csv(filename)
    return df

filename = '/Users/kamalia/PycharmProjects/Charts with matplotlib/StepByStepProject/Project/dataset.csv'

def required_columns(df):
    return df[['name', 'platform', 'genre']]

# Step3
def interested_platforms(df):
    platforms_of_interest = ['PS4', 'XOne', 'PC', 'WiiU']
    df['platform'] = pd.Categorical(df['platform'], categories=platforms_of_interest, ordered=True)
    df_filtered = df[df['platform'].isin(platforms_of_interest)]
    return df_filtered

df = load_the_data(filename)
df = required_columns(df.copy())
df = interested_platforms(df.copy())


