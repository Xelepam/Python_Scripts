# -*- coding: utf-8 -*-

"""
Created on Sun Nov 19 13:36:53 2017

@author: Omar Enrique Castro, E.I.T
"""
####################################
###                              ###
###  Multiple Linear Regression  ###
###                              ###
####################################


# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing Dataset
dataset = pd.read_csv('/Users/omare.castro/Udemy/Machine Learning - Hands On Python & R in Data Science/Part 2 - Regression/Section 5 - Multiple Linear Regression/50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values


# Encoding Categorical Data - Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()   


# Avoiding the Dummy Variable Trap
X = X[:, 1:]


# Splitting the Dataset into the Training Set and Test Set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# Predicting the Test Set Results
y_pred = regressor.predict(X_test)


# Building the Optimal Model Using Backward Elimination 
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X , axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
