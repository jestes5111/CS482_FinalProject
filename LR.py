import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# open the file
file = pd.read_csv("C:/Users/mburl/Desktop/ml project/data.csv")

# save the data as a np array
data = file.to_numpy()

# slice the data for easier reading
X = data[:, :-2]
y = data[:, -1]

# use an 80/20 split for training and testing data

# create and train the model with cross validation
result = LogisticRegression(max_iter=2000)
scores = cross_val_score(result, X, y, cv=5)
# save the train and test with cross valiation scores
print("Average score: {0}".format(np.mean(scores)))
