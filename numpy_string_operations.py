import numpy as np

name = "Md. Abdullah Al "
str1 = "Arif"

st_add = np.char.add(name, str1)
print(st_add, st_add.size, type(st_add))

lower = np.char.lower(st_add)
print(lower)

upper = np.char.upper(st_add)
print(upper)

center = np.char.center(st_add, 50, fillchar='*')
print(center)



