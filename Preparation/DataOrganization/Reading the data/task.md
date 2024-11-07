
#### General Info about Reading Data

In **pandas**, one of its core strengths is the ability to read and manipulate data from various file formats like **CSV**, **Excel**, **JSON**, and more. The `pandas` library provides convenient functions to load and parse these files into **DataFrames**. This makes it easy to work with real-world datasets directly from different sources.

Here’s a summary of commonly used functions to read data into pandas:

1. **CSV files**:
   - The `pd.read_csv()` function reads comma-separated values (CSV) files into a DataFrame. This is one of the most frequently used methods for importing data.
   - It is essential to keep the 'data.csv' file in the same directory with the file, where you call the function. Alternatively, you can write the whole path to the 'data.csv' file. 
   ```
   df = pd.read_csv('data.csv')
   ```

2. **Excel files**:
   - The `pd.read_excel()` function reads data from Excel files. You can specify which sheet to read if there are multiple sheets in the workbook.
   ```
   df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
   ```

3. **JSON files**:
   - The `pd.read_json()` function reads JSON (JavaScript Object Notation) formatted data.
   ```
   df = pd.read_json('data.json')
   ```

4. **SQL databases**:
   - Pandas can also read data directly from SQL databases using the `pd.read_sql()` function.
   ```
   import sqlite3
   conn = sqlite3.connect('my_database.db')
   df = pd.read_sql('SELECT * FROM my_table', conn)
   ```

5. **Other formats**:
   - Pandas also supports other formats like **HTML**, **parquet**, **HDF5**, etc., which are less commonly used but very useful in specific contexts.

