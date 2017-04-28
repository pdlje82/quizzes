'''LabelEncoder is a utility class to help normalize labels such that they
contain only values between 0 and n_classes-1. This is sometimes useful for
writing efficient Cython routines. LabelEncoder can be used as follows:'''

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
le.fit([1, 2, 2, 6, 7, 8, 8])
print le.classes_
print le.transform([1, 1, 2, 6, 8, 8, 8])
print le.inverse_transform([0, 0, 1, 2, 3, 3, 3])

'''It can also be used to transform non-numerical labels (as long as they
are hashable and comparable) to numerical labels:'''

print''
le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])
print list(le.classes_)
print le.transform(["tokyo", "tokyo", "paris"])
print list(le.inverse_transform([2, 2, 1]))
print''
print''

'''Convert categorical features to features that can be used with scikit-learn estimators
with one-of-K or one-hot encoding, which is implemented in OneHotEncoder. This estimator
transforms each categorical feature with m possible values into m binary features, with only one active.'''

enc = preprocessing.OneHotEncoder()
A = [[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]]
print A
enc.fit(A)
print enc.transform([[0, 1, 3]]).toarray()
