import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression

# open the file
file = pd.read_csv('collected_data.csv')

# save the data as a np array
data = file.to_numpy()

# slice the data for easier reading
X = data[:, :-2]
y = data[:, -1]

# use an 80/20 split for training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create and train the model with cross validation
classifier = LogisticRegression(penalty='none', cv=5, max_iter=2000)
classifier.fit(X_train, y_train)

# save the train and test with cross valiation scores
train_score = cross_val_score(classifier), X_train, y_train)
test_score = cross_val_score(classifier, X_test, y_test)

# print the scores
print('Training score:', np.mean(train_score))
print('Testing score:', np.mean(test_score))
