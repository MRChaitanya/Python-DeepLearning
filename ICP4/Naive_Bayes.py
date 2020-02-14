import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('glass.csv')

X_train = data.drop("Type", axis=1)
Y_train = data["Type"]


X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.4, random_state=0)


nav = GaussianNB()
y_pred = nav.fit(X_train, Y_train).predict(X_test)
acc_knn = round(nav.score(X_train, Y_train) * 100, 2)
print("NAV accuracy is:",acc_knn)
