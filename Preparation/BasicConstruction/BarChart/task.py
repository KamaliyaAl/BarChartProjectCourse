import matplotlib.pyplot as plt

def define_data():
    categories = ['A', 'B', 'C', 'D']  # X
    values = [25, 40, 35, 20]  # Y
    return categories, values

def create_bar_chart(categories, values, width, color, orientation):
    if orientation == 'vertical':
        plt.bar(categories, values, color=color, width=width)
    elif orientation == 'horizontal':
        plt.barh(categories, values, color=color, height=width)

def add_labels_and_title(xlabel, ylabel, title):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

def show_chart():
    plt.show()

categories, values = define_data()
create_bar_chart(categories, values, 0.6, 'blue', 'vertical')
add_labels_and_title('Categories', 'Values', 'Simple Bar Chart Example')
show_chart()
