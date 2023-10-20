import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv('chaya.csv')

# Group data by Cart_Abandonment_Factors and count the number of abandoned carts
abandonment_counts = data['Cart_Abandonment_Factors'].value_counts()

# Sort the abandonment factors by the number of abandoned carts (descending order)
abandonment_counts = abandonment_counts.sort_values(ascending=False)

# Create a bar graph with the y-axis representing cart abandonment factors
fig, ax = plt.subplots(figsize=(10, 6))
abandonment_counts.plot(kind='barh', ax=ax)  # 'barh' for horizontal bar chart

# Add labels and a title
ax.set_ylabel('Cart Abandonment Factors')
ax.set_xlabel('Count')
ax.set_title('Distribution of Cart Abandonment Factors')

# Show the plot
plt.tight_layout()
plt.show()
