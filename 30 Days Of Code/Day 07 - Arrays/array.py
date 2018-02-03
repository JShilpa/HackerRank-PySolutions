# https://www.hackerrank.com/challenges/30-arrays/problem
#!/bin/python3

import sys
def reverse_array(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        print(str(arr[i]), end = ' ')


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
reverse_array(arr)



