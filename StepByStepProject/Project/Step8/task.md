## Customization
# Task: Display Bar Chart of Games by Genre and Platform

In this task, you will implement a function to display a bar chart that shows the number of games by genre for specific platforms.

## Steps:

1. **Show Bar Chart**:
- Implement a function called `show_bar(df)` that encapsulates all the previous steps required to prepare and display the bar chart.
- This function should:
  - Call `required_columns(df)` to extract the relevant columns from the DataFrame.
  - Filter the DataFrame for specific platforms using `interested_platforms(df)`.
  - Group the filtered data by platform and genre using `group_data(df)`.
  - Prepare the bar chart details with `bar_chart_details(grouped_data)`.
  - Set the positions of the bars using `set_positions(bar_width, platforms, genres, colors, grouped_data)`.
  - Configure the bar chart settings with `bar_settings(bar_width, platforms, genres, x_positions)`.
  - Optionally: Use `plt.tight_layout() ` to make sure that there will be no overlap
  - Finally, call `plt.show()` to display the chart.
