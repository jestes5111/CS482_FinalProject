import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV

# open the file
file = pd.read_csv("DSL-StrongPasswordData-modified.csv")

# save the data as a np array
data = file.to_numpy()

# use an 80/20 split for training and testing data
X_train, X_test, y_train, y_test = train_test_split(data[:, 0:-2], data[:, -1])

# create and train the model with cross validation
lr_cv = LogisticRegressionCV(cv = 5, max_iter = 1000)
lr_cv.fit(X_train, y_train)

# save the train and test scores
cv_train_score = lr_cv.score(X_train, y_train)
cv_test_score = lr_cv.score(X_test, y_test)

# print the scores
print("Training score:", cv_train_score)
print("Testing with cross validation score:", cv_test_score)
