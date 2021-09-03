import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.preprocessing import LabelEncoder

# open the file
file = pd.read_csv("DSL-StrongPasswordData(1).csv")

# save the data as a np array
data = file.to_numpy()

# create a Label Encoder to make the data usable
#lab_enc = LabelEncoder()

# create empty lists to save results to
train_result = []
test_result = []

# use an 80/20 split for training and testing data
X_train, X_test, y_train, y_test = train_test_split(data[:, 0:-2], data[:, -1])
print("data split completed")
# create and train the model
lr = LogisticRegression(max_iter=1000).fit(X_train, y_train)
print("LR fit completed")
train_score = lr.score(X_train, y_train)
test_score = lr.score(X_test, y_test)
print("train score", train_score, 'test score', test_score)
