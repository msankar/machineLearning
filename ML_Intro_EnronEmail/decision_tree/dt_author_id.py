#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy as np
import pylab as pl
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf = clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
l = len(features_train[0])
print l
print features_train

t0 = time()
pred = clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"

### you fill this in!
### be sure to compute the accuracy on the test set
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc

    



