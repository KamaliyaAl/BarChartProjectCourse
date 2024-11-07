## Customization
# Task: Configure Bar Chart Settings

In this task, you will implement a function to configure the settings for the bar chart, including labels, titles, and grid lines.

## Steps:

1. **Configure Bar Chart Settings**:

- Implement a function called `bar_settings(bar_width, platforms, genres, x_positions)` that sets up the chart's appearance.
- The function should:
  - Label the x-axis as "Platforms" and the y-axis as "Number of Games".
  - Set the chart title to "Number of Games by Genre and Platform".
  - Configure the x-ticks to display the platform names at appropriate positions.
  - Add a legend indicating the genres.
  - Enable a grid for the y-axis for better readability. Use this properties as well: linestyle=':', alpha=0.7
- Optionally:
  - For xlabel and ylabel I recommend to use these properties: fontsize=12, fontweight='bold'
  - For title: fontsize=15, fontweight='bold'
  - For x-ticks: fontsize=10
  - For legend: loc='upper right', fontsize=10
 
  
2. **Run the Code**:
- Use the `bar_settings` function after setting the bar positions to configure the chart's appearance.

<div class="hint">
  For x-ticks make sure that you use plt.xticks correctly:

```
 plt.xticks(x_positions + bar_width * (len(genres) - 1) / 2, platforms, fontsize=10)
```
</div>