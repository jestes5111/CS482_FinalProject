import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt






csv=pd.read_csv("Target_S002.csv")
data=csv.to_numpy()
result_train=[]
result_test=[]
x_train,x_test, y_train,y_test=train_test_split(data[:,0:-2],data[:,-1])
for i in range(1,200):
     clf = KNeighborsClassifier(n_neighbors=i)
     clf.fit(x_train,y_train)
     result_train.append(clf.score(x_train, y_train))
     result_test.append(clf.score(x_test, y_test))
     print(clf.score(x_test, y_test))
plt.plot(result_test,label='test accuracy')
plt.plot(result_train,label='training accuracy')
plt.legend()
plt.show()

#X is the features, Y is the result array, and the target is the category I am interested in


        
