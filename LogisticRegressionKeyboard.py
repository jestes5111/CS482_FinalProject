import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.preprocessing import LabelEncoder

# open the file
file = pd.read_csv("DSL-StrongPasswordData-test.csv")

# save the data as a np array
data = file.to_numpy()

# create a Label Encoder to make the data usable
#lab_enc = LabelEncoder()

# create empty lists to save results to
train_result = []
test_result = []

# use an 80/20 split for training and testing data
X_train, X_test, y_train, y_test = train_test_split(data[:, 2:], data[:, 0])

# create and train the model
lr = LogisticRegression().fit(X_train, y_train)

# loop through all entires
for i in range(data.size):
    # save the scores for train and test data
    train_score = lr.score(X_train, y_train)
    test_score = lr.score(X_test, y_test)

    # append the scores to the lists
    train_result.append(train_score)
    test_result.append(test_score)

# plot the training and testing accuracy
plt.plot(train_result, label = "Training accuracy")
plt.plot(test_result, label = "Testing accuracy")

# show the legend
plt.legend()
