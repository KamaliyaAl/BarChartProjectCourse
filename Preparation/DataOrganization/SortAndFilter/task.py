import pandas as pd

data = {
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Keyboard'],
    'Price': [1200, 350, 800, 250, 100],
    'Stock': [50, 100, 200, 150, 500]
}

df = pd.DataFrame(data)

def sort_by_stock_and_price(df):
    return df.sort_values(by=['Stock', 'Price'], ascending=True)

def filter_by_stock_and_price(df):
    return df[(df['Stock'] > 100) & (df['Price'] < 1000)]

def filter_by_product_name(df):
    return df[df['Product'].str.contains('phone', case=False)]

sorted_df = sort_by_stock_and_price(df)
filtered_df_stock_price = filter_by_stock_and_price(df)
filtered_df_product = filter_by_product_name(df)

print("Sorted DataFrame:\n", sorted_df)
print("\nFiltered by Stock > 100 and Price < 1000:\n", filtered_df_stock_price)
print("\nFiltered by Product containing 'phone':\n", filtered_df_product)
