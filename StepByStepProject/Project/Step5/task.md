## Chart Creation
*Task: Prepare Data for a Bar Chart*

In this task, you will set up the necessary components to create a bar chart visualizing the grouped data by `platform` and `genre`.

## Steps:

1. **Prepare Bar Chart Details**:
- Implement a function called `bar_chart_details(grouped_data)` that prepares the details required to create a bar chart.
- The function should calculate the 'bar_width' = 0.2, and the positions for the platforms on the x-axis.
- Use `numpy` to create an array of positions for the platforms.
- Determine the colors for the bars using the `tab20` colormap from `matplotlib.get_cmap()` functions. Set as many colors as genres
- Return everything you declared

2. **Run the Code**:
- Use the `bar_chart_details` function with the grouped data obtained from the previous task to get the necessary details for plotting.


<div class="hint">

you can use `df.index` and `df.columns` for platform and genres respectively

</div>