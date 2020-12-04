import math, time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

start = time.time()
#lists to hold accuracies and test sizes for plotting
Yaccur = []
Xtsize = []
#loop through .1-.9 test sizes and record accuracies
for x in range(8):

    #load in the data set and print out the top portion + dimensions(shape)
    MNIST_train_small_df = pd.read_csv('mnist_subset.csv', sep=',', index_col=0)
    print (MNIST_train_small_df.head(3))
    print (MNIST_train_small_df.shape)
    #ensures dataframe is properly set between commas
    X_tr = MNIST_train_small_df.iloc[:,:] # iloc ensures X_tr will be a dataframe
    y_tr = MNIST_train_small_df.index

    #print ("y_tr value", y_tr.value_counts())
    #print("X_tr shape", X_tr.shape)




    #generate test size float from x
    x = (x+1)/10

    #split data from earlier into 4 subsets
    X_train, X_test, y_train, y_test = train_test_split(X_tr, y_tr, test_size=x, random_state=30, stratify=y_tr)
    print("X_train \n", X_train)
    print("X_test \n", X_test)

    #if index is >0, change to 1 to normalize data
    X_train[X_train>0]=1
    X_test[X_test>0]=1
    print("X_train after \n:", X_train)

    #calls SVC method and trains data then predicts test data

    clf = svm.SVC(kernel="poly")
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    #compares prediction with text data and displays matrix of precision/accuracy
    from sklearn.metrics import classification_report, confusion_matrix
    Xtsize.append(x)
    Yaccur.append(accuracy_score(y_test, y_pred))

#end for

plt.plot(Xtsize,Yaccur)
plt.xlabel("Test size")
plt.ylabel("Accuracy")
plt.title("SVM accuracy using poly kernel with varying Test sizes")

plt.show()