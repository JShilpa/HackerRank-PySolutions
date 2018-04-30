# Numpy Zeros and Ones Array
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np

n = tuple(map(int, input().split()))

print(np.zeros(n,dtype=np.int))
print(np.ones(n,dtype=np.int))
