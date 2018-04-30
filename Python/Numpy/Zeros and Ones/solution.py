# Numpy Zeros and Ones Array
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np

n = list(map(int, input().split()))

# Print array of zeros
print(np.zeros(n, dtype=np.int))

# Print array of ones
print(np.ones(n, dtype=np.int))
