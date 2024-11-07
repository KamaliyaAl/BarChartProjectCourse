import matplotlib.pyplot as plt

# Define data
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 35, 20]

# Create bar chart
plt.bar(categories, values, color='blue', width=0.6)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart Example')

# Display the chart
plt.show()