### General Info about Series

In **pandas**, a **Series** is a one-dimensional labeled array that can hold any data type, such as integers, floats, strings, or even objects. Each element in a Series is associated with an **index**, which can be either an integer or a label.

**Key Features of Series:**
- **Homogeneous data**: A Series contains elements of the same type (e.g., all integers, floats, etc.).
- **Labeled data**: The elements in a Series are associated with an index, making it easy to access individual elements by index.
- **Indexing**: Series can be indexed by integers, labels, or slices, similar to Python lists and NumPy arrays.
- **Missing data support**: A Series can handle missing data, typically represented by `NaN` (Not a Number).

Here’s how to create a basic Series in pandas:

```
import pandas as pd

# Creating a simple Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)

# Creating a Series with custom indices
s_with_index = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

print(s)
print(s_with_index)
```
