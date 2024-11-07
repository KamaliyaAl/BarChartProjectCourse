import pandas as pd
data = {
         'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor'],
         'Price': [1000, 300, 500, 200],
         'Stock': [50, 100, 200, 150]
}
def create_df(data):
    return pd.DataFrame(data)

def select_columns(df, columns):
    return df[columns]


def add_column(df):
    df['Total Value'] = df['Price']*df['Stock']
    return df


df = create_df(data)
selected_df = select_columns(df.copy(), ['Product', 'Price'])
df = add_column(df.copy())
