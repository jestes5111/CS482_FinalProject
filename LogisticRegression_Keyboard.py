import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# open the file
file = pd.read_csv("DSL-StrongPasswordData-modified.csv")

# save the data as a np array
data = file.to_numpy()

# use an 80/20 split for training and testing data
X_train, X_test, y_train, y_test = train_test_split(data[:, 0:-2], data[:, -1])

# create and train the model with no cross validation and l2 penalty
lr_l2 = LogisticRegression(penalty = 'l2', max_iter = 1000).fit(X_train, y_train)

# create and train the model with no cross validation and no penalty
lr_none = LogisticRegression(penalty = 'none', max_iter = 1000).fit(X_train, y_train)

# save the train and test scores
l2_train_score = lr_l2.score(X_train, y_train)
l2_test_score = lr_l2.score(X_test, y_test)
none_train_score = lr_none.score(X_train, y_train)
none_test_score = lr_none.score(X_test, y_test)

# print the scores
print("L2 Penalty Training score:", l2_train_score)
print("L2 Penalty Testing score:", l2_test_score)
print("No Penalty Training score:", none_train_score)
print("No Penalty Testing score:", none_test_score)
