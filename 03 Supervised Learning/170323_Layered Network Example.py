
import numpy as np

in_Lr = np.array([1,2,3])
hid_1_Lr_w = np.array([[1],[1],[-5]])
hid_2_Lr_w = np.array([[3],[-4],[2]])
out_Lr_w = np.array([2,-1])

a = np.concatenate((hid_1_Lr_w, hid_2_Lr_w), axis=1)

b = np.dot(in_Lr, a)

c = np.dot(b, out_Lr_w.T)

#print c

d = np.array([[3, -1, 3],[2, 4, -5]])
e = np.array([1, 2, -1]).T
f = np.dot(d,e)
print f