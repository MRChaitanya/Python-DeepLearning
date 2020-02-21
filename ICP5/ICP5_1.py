import numpy as np
import pandas as pd
train = pd.read_csv('train.csv')
print ("Train data shape:", train.shape)
import matplotlib.pyplot as plt

var ='GarageArea'
data = pd.concat([train['SalePrice'], train[var]], axis=1)
plt.scatter(x=train['GarageArea'], y=train['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground living area')
plt.show()

from scipy import stats
z = np.abs(stats.zscore(data))
print(z)
threshold=3
print(np.where(z>3))


Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

data = data[(z < 3).all(axis=1)]

data_df_out = data[~((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]

print(data.shape)
print(data_df_out.shape)

var ='GarageArea'
plt.scatter(x=data['GarageArea'], y=data['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground ')
plt.show()

plt.scatter(x=data_df_out['GarageArea'], y=data_df_out['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground ')
plt.show()