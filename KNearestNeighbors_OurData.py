import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# open the file
file = pd.read_csv("ourdata.csv")

# save the data as a np array
data = file.to_numpy()

# slice the data for easier reading
X = data[:, :-2]
y = data[:, -1]

# use an 80/20 split for training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# create lists to save results for every number of neighbors
results_train = []
results_test = []

# loop to test up different numbers of neighbors
for i in range(1, 200):
    # create and train the model
    classifier = KNeighborsClassifier(n_neighbors = i).fit(X_train, y_train)

    # save the scores
    score_train = classifier.score(X_train, y_train)
    score_test = classifier.score(X_test, y_test)
    
    # append the results to the respective list
    results_train.append(score_train)
    results_test.append(score_test)

    # print the test score
    #print("Test score for k =", i, ":", score_test)

# plot the accuracy for both scores
plt.plot(results_test, label = 'test accuracy')
plt.plot(results_train, label = 'training accuracy')
plt.legend()

# show the plots in a separate window
plt.show()
