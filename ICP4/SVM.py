import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

glass = pd.read_csv('glass.csv')

X_train = glass.drop("Type", axis=1)

Y_train = glass["Type"]
X_test = X_train.drop("Fe", axis=1).copy()

X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.2, random_state=0)


svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print("svm accuracy is:", acc_svc)