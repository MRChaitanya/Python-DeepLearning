import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('winequality-red.csv')
data = train.select_dtypes(exclude=[np.number])
features = list(data.columns)
le = LabelEncoder()

for i in features:
    train[i] = le.fit_transform(train[i])
data = train.select_dtypes(include=[np.number]).interpolate().fillna(train.select_dtypes(include=[np.number]).interpolate().mean(axis=0))

from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
scaler.fit(data)
x = scaler.transform(data)

from sklearn.cluster import KMeans

clusters = 3
seed = 0
km = KMeans(n_clusters=clusters, random_state=seed)
km.fit(x)
y_cluster_kmeans = km.predict(x)

from sklearn import metrics

score = metrics.silhouette_score(x, y_cluster_kmeans)
scores = metrics.silhouette_samples(x, y_cluster_kmeans)
print("Silhoutte score", score)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=500, n_init=10, random_state=0)
    kmeans.fit(data)
    cluster_an = kmeans.predict(data)
    wcss.append(kmeans.inertia_)

scaler = preprocessing.StandardScaler()
scaler.fit(x)
x_scaled_array = scaler.transform(x)
x_scaled = pd.DataFrame(x_scaled_array)
feature_scaling_score = metrics.silhouette_score(x_scaled, y_cluster_kmeans)
print(feature_scaling_score)

from sklearn.decomposition import PCA

pca = PCA(2)
x_pca = pca.fit_transform(x_scaled)

km_1 = KMeans(n_clusters=3, random_state=0)
km_1.fit(x_pca)
kmeans_1 = km_1.predict(x_pca)

y_cluster_kmeans_1 = km_1.predict(x_pca)


import matplotlib.pyplot as plt

plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

plt.scatter(y_cluster_kmeans, scores, alpha=.75,
            color='b')
plt.xlabel('Cluster')
plt.ylabel('Scores')
plt.show()

plt.scatter(range(1, len(y_cluster_kmeans) + 1), y_cluster_kmeans, alpha=.75,
            color='b')
plt.xlabel('Id')
plt.ylabel('Cluster')
plt.show()

plt.hist(y_cluster_kmeans, color="blue")
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('K-Means Model')
plt.show()
