
#### Common Use Case: Sorting and Filtering Combined

In real-world data analysis, sorting and filtering are often used together. For instance, you might want to filter a dataset to focus on a particular group and then sort that group by a specific column to analyze the results.

```
# Filtering rows where 'Age' is greater than 30 and then sorting by 'Salary'
df_filtered_sorted = df[df['Age'] > 30].sort_values(by='Salary', ascending=False)
```

### Tasks to Practice Sorting and Filtering

1. **Task 1: Sorting a DataFrame**
   - **Create a function `sort_by_stock_and_price`** which takes a DataFrame as an argument. Sort the DataFrame by 'Stock' and 'Price' in ascending order and return the sorted DataFrame.
   - **Create a function `filter_by_stock_and_price`** which takes a DataFrame as an argument. Return a filtered DataFrame where 'Stock' is greater than 100 and 'Price' is less than 1000.
   - **Create a function `filter_by_product_name`** which takes a DataFrame as an argument. Filter the DataFrame to return only rows where the 'Product' name contains 'phone' (case-insensitive).