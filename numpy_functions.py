import numpy as np

# arrange()
ar_1d = np.arange(1,13)         # .arrange(start,end<excluded>, steps)
print(ar_1d)

even_array = np.arange(1,13,2)
print(even_array)

# linspace()
random_arr5 = np.linspace(1, 3, 5)      # 5 random value in the range of 1 and 3 with same difference
print(random_arr5)

# reshape [1D array ---> MultiDim Array]
arr_2d = ar_1d.reshape(3, 4)         # 1D array to 2d (3x4 matrix) array
print(arr_2d)

ar_3d = ar_1d.reshape(3, 2, 2)
print(ar_3d)

# ravel()   [MultiDim array ---> 1D array]
masked_1d = ar_3d.ravel()
print(masked_1d)


# flatten() [make the matrix flat]
print(ar_3d.flatten())

#   Transpose
arr_2d_trans = arr_2d.transpose()  # arr_2d.T
print(arr_2d_trans)