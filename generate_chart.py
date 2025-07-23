import matplotlib.pyplot as plt

# Sample data
categories = ['Apples', 'Bananas', 'Oranges']
values = [30, 50, 20]

# Create a bar chart
plt.bar(categories, values, color='skyblue')
plt.title('Fruit Sales')
plt.xlabel('Fruit')
plt.ylabel('Sales')
plt.savefig('chart.png')  # Save the chart as an image
plt.close()