import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


data = pd.read_csv('corona_data.csv')

x1 = data.drop('Date', axis=1)
x2 = x1.drop('Last Update', axis=1)
x3 = x2.drop('Country', axis=1)
x4 = x3.drop('Province/State', axis=1)

x4 = x4.drop_duplicates()
x4 = x4.dropna()
x4 = x4.drop("Deaths", axis=1)
y = x4.isnull().values.any()
print(y)



from sklearn.neighbors import KNeighborsClassifier

X_train = x4.drop("Confirmed", axis=1)
Y_train = x4["Confirmed"]


X_test = x4.drop("Recovered",axis=1).copy()

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
print("KNN accuracy is:",acc_knn)


X_train = x4.drop("Confirmed", axis=1)
Y_train = x4["Confirmed"]

X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.4, random_state=0)

nav = GaussianNB()
y_pred = nav.fit(X_train, Y_train).predict(X_test)
acc_knn = round(nav.score(X_train, Y_train) * 100, 2)
print("NAV accuracy is:", acc_knn)

from sklearn.svm import SVC

svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print("svm accuracy is:", acc_svc)
