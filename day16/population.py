import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Foodtruck.csv")
#print dataset.describe()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Splitting
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#   Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results,compare it with y_test
y_pred = regressor.predict(X_test)
print (y_pred)


# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'red')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

