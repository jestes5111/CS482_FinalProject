import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# open the file
file = pd.read_csv("DSL-StrongPasswordData-modified.csv")

# save the data as a np array
data = file.to_numpy()

# slice the data for easier reading
X = data[:, :-2]
y = data[:, -1]

# use an 80/20 split for training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create and train the model with no cross validation and l2 penalty
classifier_l2_penalty = LogisticRegression(penalty='l2', max_iter=1000)
classifier_l2_penalty.fit(X_train, y_train)

# create and train the model with no cross validation and no penalty
classifier_no_penalty = LogisticRegression(penalty='no_penalty', max_iter=1000)
classifier_no_penalty.fit(X_train, y_train)

# save the train and test scores
train_score_l2_penalty = classifier_l2_penalty.score(X_train, y_train)
test_score_l2_penalty = classifier_l2_penalty.score(X_test, y_test)
train_score_no_penalty = classifier_no_penalty.score(X_train, y_train)
test_score_no_penalty = classifier_no_penalty.score(X_test, y_test)

# print the scores
print("L2 Penalty Training score:", train_score_l2_penalty)
print("L2 Penalty Testing score:", test_score_l2_penalty)
print("No Penalty Training score:", train_score_no_penalty)
print("No Penalty Testing score:", test_score_no_penalty)
