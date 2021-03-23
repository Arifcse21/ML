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

print(np.random.randint(1, 5, (3, 3)))  # values (1-4) IN 3X3 array
# print(random.randint(1, 5, (4, 4)))
# ###################################################################
# As everytime the random.randint() is different. We need to seed a label
np.random.seed(22)      # seed value can be 2**64 -1
print(np.random.randint(1, 4, (4, 4)))


np.random.seed(22)      # seed value can be 2**64 -1
print(np.random.randint(1, 4, (4, 4)))

# ####################################################################

print(np.random.rand(3, 3))     # random 3x3 array
print(np.random.randn(4, 4))    # random(pos+neg) 3x3 array

# #######CHOICE#######

x = [1, 2, 5, 7]
print(np.random.choice(x))

# ###########Permutation############
print(np.random.permutation(x))
# print(np.random.shuffle(x))


