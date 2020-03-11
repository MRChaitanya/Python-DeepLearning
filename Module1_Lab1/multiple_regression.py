import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error

data = pd.read_csv('corona_data.csv')
x1 = data.drop('Date', axis=1)
x2 = x1.drop('Last Update',axis=1)
x3 = x2.drop('Country',axis=1)
x4 = x3.drop('Province/State', axis=1)

y = x4.isnull().values.any()
print(y)
x4 = x4.drop_duplicates()
x4 = x4.dropna()

X_train = x4.drop('Confirmed', axis=1)
Y_train = x4['Confirmed']

regr = linear_model.LinearRegression()

regr.fit(X_train, Y_train)
y_pred = regr.predict(X_train)

print("Variance score: %.2f" % r2_score(Y_train,y_pred))
print("Mean squared error: %.2f" % mean_squared_error(Y_train,y_pred))


