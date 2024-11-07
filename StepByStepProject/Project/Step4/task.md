## Data Preparation
# Task: Group Data by Platform and Genre

In this task, you will group the dataset by `platform` and `genre` and return the count of entries for each combination.

This guide provides a brief overview of three essential Pandas functions: `groupby`, `size`, and `unstack`. These functions are used together to efficiently summarize and reshape data in a DataFrame.

- **`groupby`**: Groups data by specified columns.
- **`size`**: Counts occurrences in each group.
- **`unstack`**: Transforms groups into a table with new columns.


## Steps:

1. **Group Data**:
- Implement a function called `group_data(df)` that groups the DataFrame by `platform` and `genre`.
- Use the `groupby()` method to create groups, and then use `size()` to count the number of entries in each group.
- Use `unstack()` to reshape the data for better readability, filling any missing values with `0`.

2. **Run the Code**:
- Use the `group_data` function to obtain and display the grouped data.
