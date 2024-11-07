
### Several Manipulations with DataFrames

```
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
```

Once a DataFrame is created, various operations can be performed, such as filtering, selecting specific columns, or performing aggregations. Here are some common manipulations:

1. **Accessing specific columns**:
   You can access a specific column using its label (name).

```
# Accessing the 'Name' column
names = df['Name']
print(names)  # Output: Series containing the names ['Alice', 'Bob', 'Charlie', 'David']
```

2. **Accessing rows**:
   Rows can be accessed using the `.loc[]` (label-based) or `.iloc[]` (integer position-based) methods.

```
# Accessing the first row using integer position
print(df.iloc[0])   # Output: Series with data of the first row [Alice, 25, 50000]

# Accessing a row by index label
df_with_index = df.set_index('Name')
print(df_with_index.loc['Bob'])  # Output: Series with data of Bob's row [Bob, 30, 60000]
```

3. **Selecting multiple columns**:
   You can select multiple columns by passing a list of column names.

```
# Selecting 'Name' and 'Salary' columns
selected_columns = df[['Name', 'Salary']]
print(selected_columns)
```

4. **Adding new columns**:
   New columns can be added by assigning values to a new column name.

```
# Adding a 'Bonus' column
df['Bonus'] = df['Salary'] * 0.1
print(df)  # Output: DataFrame with an additional 'Bonus' column
```

5. **Basic mathematical operations**:
   Operations can be applied to entire columns, similar to Series.

```
# Giving a 5% raise to all salaries
df['Salary'] = df['Salary'] * 1.05
print(df)  # Output: DataFrame with updated salaries
```

6. **Handling missing data**:
   Missing values in a DataFrame can be detected and handled through various methods.

```
# Creating a DataFrame with missing values
data_with_nan = {
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, None, 35, 40],
    'Salary': [50000, 60000, None, 80000]
}
df_nan = pd.DataFrame(data_with_nan)

# Checking for missing values
print(df_nan.isnull())  # Output: DataFrame with boolean values indicating missing data

# Filling missing values in the 'Age' column
df_nan['Age'].fillna(30, inplace=True)
print(df_nan)  # Output: DataFrame with missing values in 'Age' filled
```
**inplace is responsible for updating the series. For instance, we can assign the variable with altered df, but with `inplace = False` df itself stays the same**

### Tasks to Check the Obtained Knowledge

**Create and Manipulate a DataFrame**
- **Create a function `create_df`** which takes a dictionary as an argument containing lists for 'Product', 'Price', and 'Stock'. Return a Pandas DataFrame created from this data.
- **Create a function `select_columns`** which takes a DataFrame and a list of column names as arguments. Return a DataFrame containing only the specified columns.
- **Create a function `add_column`** which takes a DataFrame as an argument and adds a new column 'Total Value' calculated as 'Price' multiplied by 'Stock'. Return the updated DataFrame.

