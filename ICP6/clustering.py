import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('CC.csv')
s = data['MINIMUM_PAYMENTS'].isnull().sum()
j = data['CREDIT_LIMIT'].isnull().sum()
c= data['MINIMUM_PAYMENTS'].mean()
d= data['CREDIT_LIMIT'].mean()
data= data.apply(lambda s:s.fillna(c),axis=0)
data = data.apply(lambda j:j.fillna(d),axis=0)

l=data.isnull().sum()
print(l)

wcss= []

x = data.iloc[:,1:17]
y = data.iloc[:,-1]
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,max_iter=100, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('wcss')
plt.show()

km =KMeans(n_clusters=3, random_state=0)
km.fit(x)
kmeans=km.predict(x)



y_cluster_kmeans= km.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)

from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
x_scaled_array = scaler.transform(x)
x_scaled = pd.DataFrame(x_scaled_array, columns =x.columns)
feature_scaling_score = metrics.silhouette_score(x_scaled, y_cluster_kmeans)
print(feature_scaling_score)

from sklearn.decomposition import PCA
pca= PCA(2)
x_pca= pca.fit_transform(x_scaled)

km_1 =KMeans(n_clusters=3, random_state=0)
km_1.fit(x_pca)
kmeans_1=km_1.predict(x_pca)


y_cluster_kmeans_1= km_1.predict(x_pca)
from sklearn import metrics
pca_score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print(pca_score)


