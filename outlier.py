import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("chaya.csv")

# Data Summary
print(data.head())  # Display the first few rows of the dataset
print(data.describe())  # Display summary statistics

# Visualize the data using box plots
plt.figure(figsize=(12, 8))
sns.boxplot(data=data)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.title("Box Plot of Dataset Features")
plt.show()

# Detect and display outliers using z-scores
from scipy import stats
z_scores = stats.zscore(data.select_dtypes(include=['number']))
outliers = (z_scores > 3).any(axis=1)  # Adjust the threshold as needed
outlier_data = data[outliers]
print("Outliers:")
print(outlier_data)

# Visualize the outliers using a box plot
plt.figure(figsize=(12, 8))
sns.boxplot(data=outlier_data)
plt.xticks(rotation=90)
plt.title("Box Plot of Outlier Features")
plt.show()
