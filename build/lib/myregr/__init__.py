from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
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
