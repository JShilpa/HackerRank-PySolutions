#https://www.hackerrank.com/challenges/30-conditional-statements/problem

#!/bin/python3
import sys

n = int(input().strip())
if n%2 != 0:
    print('Weird')
else:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    elif n > 20:
        print("Not Weird")