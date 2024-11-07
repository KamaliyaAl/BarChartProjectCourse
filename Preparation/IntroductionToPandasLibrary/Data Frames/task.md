### General Info about DataFrames

A **DataFrame** in **pandas** is a two-dimensional, labeled data structure similar to a table, with rows and columns. It is one of the most commonly used structures in pandas because of its flexibility in handling various types of data.

**Key Features of DataFrame:**
- **Labeled axes**: A DataFrame has both row and column labels (indices). The default row index is numerical, but custom labels can also be assigned.
- **Heterogeneous data**: Unlike a Series, a DataFrame can contain different types of data in different columns (e.g., integers, floats, strings).
- **Size flexibility**: A DataFrame can be of any size, from small to large datasets.
- **Handling missing data**: DataFrames can handle missing values (e.g., `NaN`) effectively.
- **Indexing and selecting data**: You can easily access, filter, and manipulate rows and columns in a DataFrame.

Here’s how to create a basic DataFrame in pandas from a dictionary:

```
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print(df)
```
