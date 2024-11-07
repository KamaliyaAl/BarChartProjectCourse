## Data Preparation
# Task: Filter the Dataset for Specific Platforms

In this task, you will filter the dataset to include only specific platforms of interest.

## Steps:

1. **Filter for Specific Platforms**:
- Implement a function called `interested_platforms(df)` that filters the dataset to include only the following platforms: `PS4`, `XOne`, `PC`, and `WiiU`.
- Ensure the `platform` column is treated as a categorical variable with a defined order for these platforms.
- Use the `isin()` method to filter the DataFrame based on the specified platforms.

2. **Run the Code**:
- Use the `interested_platforms` function to filter the dataset and return the filtered DataFrame.


<div class="hint">
Устанавливаем порядок категорий для столбца platform:

С помощью pd.Categorical мы делаем столбец platform категориальным, задавая порядок платформ, указанный в platforms_of_interest. Это позволяет сортировать и упорядочивать данные по этим платформам.

```
df['platform'] = pd.Categorical(df['platform'], categories=platforms_of_interest, ordered=True)
```

</div>