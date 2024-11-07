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

def bar_chart_details(grouped_data):
    bar_width = 0.2
    x = np.arange(len(grouped_data.index))
    platforms = grouped_data.index
    genres = grouped_data.columns
    colors = plt.get_cmap('tab20', len(genres))
    return bar_width, x, platforms, genres, colors


def set_positions(bar_width, platforms, genres, colors, grouped_df):
    x_positions = np.arange(len(platforms)) * (bar_width * len(genres) + 0.1)
    for i, genre in enumerate(genres):
        plt.bar(x_positions + i * bar_width, grouped_df[genre], width=bar_width, label=genre,
                color=colors(i), alpha=0.8)
    return x_positions


# Step 7
def bar_settings(bar_width, platforms, genres, x_positions):
    plt.xlabel('Platforms', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Games', fontsize=12, fontweight='bold')
    plt.title('Number of Games by Genre and Platform', fontsize=15, fontweight='bold')
    plt.xticks(x_positions + bar_width * (len(genres) - 1) / 2, platforms, fontsize=10)
    plt.legend(title='Genres', loc='upper right', fontsize=10)
    plt.grid(axis='y', linestyle=':', alpha=0.7)

df = load_the_data(filename)
df = required_columns(df.copy())
df = interested_platforms(df.copy())
grouped_df = group_data(df.copy())
bar_width, x, platforms, genres, colors = bar_chart_details(grouped_df.copy())
x_positions = set_positions(bar_width, platforms, genres, colors, grouped_df)
bar_settings(bar_width, platforms, genres, x_positions)

