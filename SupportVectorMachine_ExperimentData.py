import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# open the file
input_file = pd.read_csv('DSL-StrongPasswordData-modified.csv')

# save the data as a np array
data = input_file.to_numpy()

# slice the data for easier reading
X = data[:, :-2]
y = data[:, -1]

# use an 80/20 split for training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create and train the support vector machine classifier
classifier = SVC()
classifier.fit(X_train, y_train)

# save the train and test scores
score_train = classifier.score(X_train, y_train)
score_test = classifier.score(X_test, y_test)

# print the scores
print('Training score:', score_train)
print('Testing score:', score_test)
