#### Sorting and Filtering Data in pandas

In **pandas**, sorting and filtering are two fundamental operations used to organize and extract meaningful information from data. Sorting allows you to arrange the rows of a **DataFrame** or **Series** in a specific order, while filtering enables you to focus on rows that meet specific conditions.

#### Sorting Data

Pandas provides the `sort_values()` function to sort data in a **DataFrame** or **Series** based on the values in one or more columns. Sorting can be done in ascending or descending order.

1. **Sorting by a single column**:
   You can sort a DataFrame by the values in a specific column. By default, sorting is done in ascending order.

   ```
   # Sorting by the 'Age' column in ascending order
   df_sorted = df.sort_values(by='Age')

   # Sorting by the 'Salary' column in descending order
   df_sorted_desc = df.sort_values(by='Salary', ascending=False)
   ```

2. **Sorting by multiple columns**:
   You can also sort by more than one column. For example, you can sort by `Age`, and in case of a tie, by `Salary`.

   ```
   # Sorting by 'Age' and then by 'Salary'
   df_sorted_multi = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
   ```

3. **Sorting by index**:
   You can sort a DataFrame by its index (row labels) using the `sort_index()` method.

   ```
   # Sorting by the index
   df_sorted_by_index = df.sort_index()
   ```

#### Filtering Data

Filtering data involves selecting rows that meet a certain condition. In pandas, this is done using boolean indexing, where you apply a condition to the DataFrame, and it returns only the rows that satisfy that condition.

1. **Filtering based on a single condition**:
   You can filter rows by applying a condition to one or more columns.

   ```
   # Filtering rows where 'Age' is greater than 30
   df_filtered = df[df['Age'] > 30]

   # Filtering rows where 'Salary' is equal to 60000
   df_filtered_salary = df[df['Salary'] == 60000]
   ```

2. **Filtering with multiple conditions**:
   You can combine multiple conditions using logical operators like `&` (and), `|` (or), and `~` (not). Be sure to enclose each condition in parentheses when combining multiple conditions.

   ```
   # Filtering rows where 'Age' is greater than 30 and 'Salary' is greater than 50000
   df_filtered_multi = df[(df['Age'] > 30) & (df['Salary'] > 50000)]

   # Filtering rows where 'Age' is less than 25 or 'Salary' is greater than 70000
   df_filtered_or = df[(df['Age'] < 25) | (df['Salary'] > 70000)]
   ```

3. **Filtering based on string conditions**:
   You can filter rows based on string values using string comparison.

   ```
   # Filtering rows where 'Name' is equal to 'Alice'
   df_filtered_name = df[df['Name'] == 'Alice']

   # Filtering rows where 'Name' contains the string 'li'
   df_filtered_contains = df[df['Name'].str.contains('li')]
   ```

4. **Filtering based on missing values**:
   You can filter rows with missing (`NaN`) values using `isnull()` or `notnull()`.

   ```
   # Filtering rows where 'Age' is missing
   df_missing_age = df[df['Age'].isnull()]

   # Filtering rows where 'Salary' is not missing
   df_not_missing_salary = df[df['Salary'].notnull()]
   ```
