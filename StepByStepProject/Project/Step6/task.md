## Chart Creation
*Task: Set Positions for Bar Chart*

In this task, you will implement a function to define the positions of the bars in a bar chart, accommodating multiple genres for each platform.

## Steps:

1. **Set Positions for Bar Chart**:
- Implement a function called `set_positions(bar_width, platforms, genres, colors, grouped_data)` that calculates the positions for each bar based on the number of genres.
- Use the provided bar_width to determine the position of each genre's bar for every platform.
- The function should create bars for each genre using a loop and utilize the colors generated earlier.

2. **Run the Code**:
- Use the `set_positions` function to define the positions for the bars in the bar chart.

<div class="hint">
    create bars using this command for each bar (alpha can whichever you like (I recommend 0.8):
    
```plt.bar(position, what, width=, label=,color=, alpha=)```

</div>