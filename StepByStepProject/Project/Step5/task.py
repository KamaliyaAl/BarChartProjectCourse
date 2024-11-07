import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_the_data(filename):
    df = pd.read_csv(filename)
    return df

filename = '/Users/kamalia/PycharmProjects/Charts with matplotlib/StepByStepProject/Project/dataset.csv'

def required_columns(df):
    return df[['name', 'platform', 'genre']]


def interested_platforms(df):
    platforms_of_interest = ['PS4', 'XOne', 'PC', 'WiiU']
    df['platform'] = pd.Categorical(df['platform'], categories=platforms_of_interest, ordered=True)
    df_filtered = df[df['platform'].isin(platforms_of_interest)]
    return df_filtered

def group_data(df):
    grouped_data = df.groupby(['platform', 'genre'], observed=False).size().unstack(fill_value=0)
    return grouped_data

# Step5: Create the bar chart
def bar_chart_details(grouped_data):
    bar_width = 0.2
    x = np.arange(len(grouped_data.index))
    platforms = grouped_data.index
    genres = grouped_data.columns
    colors = plt.get_cmap('tab20', len(genres))
    return bar_width, x, platforms, genres, colors


df = load_the_data(filename)
df = required_columns(df.copy())
df = interested_platforms(df.copy())
grouped_df = group_data(df.copy())
bar_width, x, platforms, genres, colors = bar_chart_details(grouped_df.copy())

