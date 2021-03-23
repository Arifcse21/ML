import numpy as np
import random


print(random.random())      # random value from 0 to 1
print(np.random.random(5))  # 5 random values in array

print(np.random.random((2, 3, 2)))      # array shape

for x in range(3):
    print(np.random.randint(5))

print()

for x in range(3):
    print(random.randint(0, 5))

print(np.random.randint(1, 5, (3, 3)))
# print(random.randint(1, 5, (4, 4)))
