import numpy as np

mx_1s = np.ones((3,5))
print(mx_1s)

mx_1s = np.ones((3,5), int)     # dtype=int,float,str, bool
print(mx_1s)

mx_1s = np.ones((3,5), bool)     # dtype=int,float,str, bool
print(mx_1s)

mx_0s = np.zeros((4,5), int)
print(mx_0s)

mx_0s = np.zeros((3,5), str)     # dtype=int,float,str, bool
print(mx_0s)

