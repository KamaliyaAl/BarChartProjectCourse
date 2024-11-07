### Several Manipulations After Reading Data

After loading the data, several operations can be performed on it, such as exploring, cleaning, and analyzing it. Let’s explore some common manipulations.

1. **Viewing the first few rows**:
   After reading data, it is common to quickly check the first few records to understand the structure.
   ```
   # Display the first 5 rows
   print(df.head())
   
   # Display the first 10 rows
   print(df.head(10))
   ```

2. **Getting summary information about the dataset**:
   You can get a quick summary of the DataFrame, including column names, data types, and the presence of missing values.
   ```
   print(df.info())  # Output: Summary info of the DataFrame
   print(df.describe())  # Output: Statistical summary of numeric columns
   ```

3. **Handling missing data**:
   After loading data, there may be missing values. These can be handled by either dropping the rows or columns or filling in the missing values.
   ```
   # Dropping rows with any missing values
   df_cleaned = df.dropna()

   # Filling missing values with a specific value
   df_filled = df.fillna(0)
   ```

### Tasks to Check the Obtained Knowledge

**Reading and Viewing Data**
   - **Create a function `read_csv_file`** which takes a file path as an argument, reads the CSV file using Pandas, and returns the DataFrame.

   - **Create a function `display_first_n_rows`** which takes a DataFrame and an integer `n` (default 7) as arguments. Return the first `n` rows of the DataFrame.

   - **Create a function `drop_missing_values`** which takes a DataFrame as an argument. Remove any rows with missing values and return the cleaned DataFrame.