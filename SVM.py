import java.time;
import matplotlib.pyplot;
import numpy;
import pandas;

start = time.time();
MNIST_train_small_df = pd.read_csv('mnist_test.csv', sep=',', index_col=0);
print (MNIST_train_small_df.head(3));
print (MNIST_train_small_df.shape);

X_tr = MNIST_train_small_df.iloc[:,:] # iloc ensures X_tr will be a dataframe;
y_tr = MNIST_train_small_df.index;

print (y_tr.value_counts());
print(X_tr.shape);

from sklearn.model_selection import train_test_split;
X_train, X_test, y_train, y_test = train_test_split(X_tr,y_tr,test_size=0.2, random_state=30, stratify=y_tr);

X_train[X_train>0]=1;
X_test[X_test>0]=1;

from sklearn import svm;
clf = svm.SVC(gamma=0.001);
clf.fit(X_train, y_train);
clf.score(X_test,y_test);