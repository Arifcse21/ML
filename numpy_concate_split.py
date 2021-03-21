import numpy as np

ar1_2d = np.arange(1, 17).reshape(4, 4)
print(ar1_2d)

ar2_2d = np.arange(17, 33).reshape(4, 4)
print(ar2_2d)

ar_con = np.concatenate((ar1_2d, ar2_2d))   # parenthesis is a must. axis = 0 by default. 0 -> coloumn
print(ar_con)

ar_con_row = np.concatenate((ar1_2d, ar2_2d), axis=1)     # axis = 1; row wise
print(ar_con_row)


ar_vertical = np.vstack((ar1_2d, ar2_2d, ar_con))
print(ar_vertical)

ar_horizontal = np.hstack((ar1_2d, ar2_2d))
print(ar_horizontal)

ar_sp = np.array_split(ar_horizontal, 4)
print(ar_sp)

print(type(ar_sp))

ar_sp_row = np.split(ar_con, 2, axis=1)
print(ar_sp_row)

d1 = np.array([3, 4, 5, 7, 8, 9, 4, 3, 5, 2, 1])
d1_sp = np.split(d1, [1, 5])
print(d1_sp)
