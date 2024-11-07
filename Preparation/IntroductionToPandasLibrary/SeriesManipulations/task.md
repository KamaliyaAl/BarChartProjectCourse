### Several Manipulations with Series

Once a Series is created, various operations can be performed on it, such as filtering, mathematical operations, or indexing. Here are some common manipulations:

1. **Accessing elements by index**:
   You can access elements using either integer positions or labels (if custom indices are used).

```
# Accessing by integer index
print(s[0])   # Output: 10

# Accessing by custom label
print(s_with_index['c'])  # Output: 30
```

2. **Slicing**:
   Similar to Python lists, you can use slicing to get a portion of the Series.

```
# Slicing based on position
print(s[1:4])   # Output: Series containing [20, 30, 40]

# Slicing based on custom index
print(s_with_index['b':'d'])  # Output: Series containing [20, 30, 40]
```

3. **Filtering based on conditions**:
   You can filter a Series by applying conditions.

```
# Filtering values greater than 30
filtered = s[s > 30]
print(filtered)   # Output: Series containing [40, 50]
```

4. **Basic mathematical operations**:
   Series support element-wise operations such as addition, subtraction, multiplication, etc.

```
# Adding a constant to each element
print(s + 10)   # Output: Series with [20, 30, 40, 50, 60]

# Multiplying each element by 2
print(s * 2)    # Output: Series with [20, 40, 60, 80, 100]
```

5. **Handling missing data**:
   Missing values in a Series are represented by `NaN`. You can check for them or fill them.

```
# Series with missing values
data_with_nan = [10, 20, None, 40, 50]
s_nan = pd.Series(data_with_nan)

# Checking for missing values
print(s_nan.isnull())  # Output: Boolean Series showing True for missing values [False, False, True, False, False]

# Filling missing values with a specific value
s_filled = s_nan.fillna(0)
print(s_filled)   # Output: Series with missing values filled with 0 [10, 20, 0, 40, 50]
```

### Tasks to Check the Obtained Knowledge
**Create a Series and Perform manipulations**
   - Create a function `create_series` which takes 2 arguments: lists of elements and indices. Create pandas Series and then slice the Series to extract values between indices 'b' and 'e' from the list with custom indices. Return the sliced Series.
   - Create a function `multiply_series` which takes Series as argument and return the Series where you multiplied each value by 2
   - Create a function `filter_series` which takes Series as argument and then filter out the values greater than 50.
