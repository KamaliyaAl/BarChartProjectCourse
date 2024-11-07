import pandas as pd

def create_series(list, indecies):
    series = pd.Series(list, index = indecies)
    return series['b':'e']

def multiply_series(series):
    return series*2

def filter_series(series):
    return series[series>50]

list = [5, 15, 25, 35, 45, 55, 65]
indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

series = create_series(list, indices)
multiplied_series = multiply_series(series.copy())
filtered_series = filter_series(series.copy())
print(filtered_series)


