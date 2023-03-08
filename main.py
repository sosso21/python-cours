from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import make_union
from sklearn.impute import MissingIndicator
from sklearn.impute import KNNImputer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import SGDClassifier
from sklearn.impute import SimpleImputer

# * SImpleImputer

X = np.array([[10, 3],
              [0, 4],
              [5, 3],
             [np.nan, 3]])

imputer = SimpleImputer(missing_values=np.nan,
                        strategy='mean')

imputer.fit_transform(X)


X_test = np.array([[12, 5],
                   [40, 2],
                   [5, 5],
                   [np.nan, np.nan]])

print("x: \n ", X)
print("X_test: \n", imputer.transform(X_test))


# * KNImputer

X = np.array([[1, 100],
             [2, 30],
             [3, 15],
             [np.nan, 20]])

imputer = KNNImputer(n_neighbors=1)
print("imputer.fit_transform(X): \n ", imputer.fit_transform(X))

X_test = np.array([[np.nan, 35]])

print("imputer.transform(X_test): \n", imputer.transform(X_test))


# * MissingIndicator

X = np.array([[1, 100],
             [2, 30],
             [3, 15],
             [np.nan, np.nan]])

MissingIndicator().fit_transform(X)


pipeline = make_union(SimpleImputer(strategy='constant', fill_value=-99),
                      MissingIndicator())

print("pipeline.fit_transform(X): \n", pipeline.fit_transform(X))

# * Application

print("===================\n \n ")

titanic = sns.load_dataset('titanic')
X = titanic[['pclass', 'age']]
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


model = make_pipeline(KNNImputer(), SGDClassifier())

params = {'knnimputer__n_neighbors': [1, 2, 3, 4]}

grid = GridSearchCV(model, param_grid=params, cv=5)

grid.fit(X_train, y_train)
grid.best_params_
