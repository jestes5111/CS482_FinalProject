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
lr = LogisticRegressionCV(cv = 5, max_iter = 1000).fit(X_train, y_train)

# save the train and test with cross valiation scores
train_score = lr.score(X_train, y_train)
test_score = lr.score(X_test, y_test)

# print the scores
print("Training score:", train_score)
print("Testing with cross validation score:", test_score)
