# Numpy Transpose & Flatten Problem
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np

N, M = map(int, input().split())
arr = [input().strip().split() for _ in range(N)]
arr = np.array(arr, int)
print(np.transpose(arr))
print(arr.flatten())
