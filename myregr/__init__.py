from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
import numpy as np


class Regression:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def linear(self):
        model = LinearRegression()
        model.fit(self.X, self.y)
        return model

    def poly(self, degree=2):
        poly = PolynomialFeatures(degree=degree)
        X_poly = poly.fit_transform(self.X)
        model = LinearRegression()
        model.fit(X_poly, self.y)
        return model

    def logistic(self):
        model = LogisticRegression()
        model.fit(self.X, self.y)
        return model

    def ridge(self, alpha=1.0):
        model = Ridge(alpha=alpha)
        model.fit(self.X, self.y)
        return model


    def multiple(self):
        model = LinearRegression()
        model.fit(self.X, self.y)
        return model



linear_model = Regression(X, y).linear()
print("Linear Regression Coefficients:", linear_model.coef_)
print("Linear Regression Intercept:", linear_model.intercept_)

poly_model = Regression(X, y).poly(degree=2)
print("Polynomial Regression Coefficients:", poly_model.coef_)
print("Polynomial Regression Intercept:", poly_model.intercept_)

logistic_model = Regression(X, y).logistic()
print("Logistic Regression Coefficients:", logistic_model.coef_)
print("Logistic Regression Intercept:", logistic_model.intercept_)

ridge_model = Regression(X, y).ridge(alpha=0.5)
print("Ridge Regression Coefficients:", ridge_model.coef_)
print("Ridge Regression Intercept:", ridge_model.intercept_)

multiple_model = reg.Regression(X, y).multiple()
print("Multiple Linear Regression Coefficients:", multiple_model.coef_)
print("Multiple Linear Regression Intercept:", multiple_model.intercept_)
