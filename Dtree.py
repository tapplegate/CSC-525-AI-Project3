from sklearn import preprocessing
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from formatData import Formatting

df1 = pd.read_csv('Titanic_training.csv', usecols=[2, 4, 5, 6, 7, 8, 9, 10, 11])
#fill in null data
#preformat data to explicits
df1 = Formatting.formatData(df1)
#format data from training  onehot set
X_onehot = pd.get_dummies(df1, drop_first=False)
#get feature names
X_onehot_names = list(X_onehot)
print(X_onehot)
#read file again without skipping columns
df1 = pd.read_csv('Titanic_training.csv')
le = preprocessing.LabelEncoder()
label_names = ["Survived", "Died"]
#transform set based on Survived column
y_coded = le.fit_transform(df1["Survived"])

#plot tree based on ID3 entropy max depth 100
dt = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
dt = dt.fit(X_onehot, y_coded)
fig, ax = plt.subplots(figsize=(10,10))
tree.plot_tree(dt, feature_names=X_onehot_names, class_names=label_names, filled=True, rounded=True, proportion=True, fontsize=10)
plt.show()
#test tree on formatting test data
df2 = pd.read_csv('Titanic_test.csv', usecols=[1,3,4,5,6,7,8,9,10])
df2 = Formatting.formatData(df2)
test_onehot = pd.get_dummies(df2, drop_first=False)
#predict test data
y_pred = dt.predict(test_onehot)
#convert test data to .csv to test accuracy
submission = pd.read_csv("DecisionTree_submission_file_template.csv")
submission["Survived"] = y_pred
submission.to_csv('submission.csv', index=False)

