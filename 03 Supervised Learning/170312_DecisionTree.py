#!/usr/bin/python
""" lecture and example code for decision tree unit """
import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the classify() function in classifyDT is where the magic
### happens-

def classify(features_train, labels_train, max_depth, min_samples_split):
    ### your code goes here--should return a trained decision tree classifer
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier(max_depth = max_depth, min_samples_split = min_samples_split)
    clf.fit(features_train, labels_train)
    return clf

clf1 = classify(features_train, labels_train, None, 2)
clf2 = classify(features_train, labels_train, 4, 20)

acc_min_samples_split_2 = clf1.score(features_test, labels_test)
acc_min_samples_split_50 = clf2.score(features_test, labels_test)

def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_20":round(acc_min_samples_split_50,3)}

acc = submitAccuracies()
print acc

#### grader code, do not modify below this line

prettyPicture(clf2, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
