import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = {
    "Value": [1, 2, 3, 10, 11]
}
df = pd.DataFrame(data)
df
X = df[['Value']].values
X
wcss = []

for k in range(1, 6):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 6), wcss, marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()
# before clustering
plt.figure()
plt.scatter(df["Value"], [0]*len(df))
plt.title("Before Clustering")
plt.xlabel("Value")
plt.yticks([])
plt.show()
kmeans = KMeans(n_clusters=2, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_
df["Cluster"]
plt.figure()
plt.scatter(df["Value"], [0]*len(df), c=df["Cluster"])
plt.scatter(centroids[:, 0], [0]*len(centroids), marker='h')
plt.title("After Clustering")
plt.xlabel("Value")
plt.show()
print("\nClustered Data:")
print(df)
wcss
