# Eye and  Identity array problem
# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy as np

# Add space
np.set_printoptions(sign=' ')

m, n = map(int, input().split(' '))

# Print the array
print(np.eye(m, n))
