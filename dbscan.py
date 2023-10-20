import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# Load your dataset
data = pd.read_csv("chaya.csv")

# Assuming you want to cluster based on 'age' and 'Shopping_Satisfaction' columns.
X = data[['age', 'Shopping_Satisfaction']].values

# Standardize the data to have zero mean and unit variance.
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Perform DBSCAN clustering
dbscan = DBSCAN(eps=0.3, min_samples=5)
cluster_labels = dbscan.fit_predict(X)

# Add the cluster labels to your dataset
data['Cluster_Labels'] = cluster_labels

# Visualize the clusters
unique_labels = set(cluster_labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

for label, color in zip(unique_labels, colors):
    data_subset = data[cluster_labels == label]
    plt.scatter(data_subset['age'], data_subset['Shopping_Satisfaction'], c=color, label=f'Cluster {label}')

plt.xlabel('Age')
plt.ylabel('Shopping Satisfaction')
plt.title('DBSCAN Clustering')

# Add a legend
plt.legend(loc='upper right', title='Cluster Labels')

plt.show()
