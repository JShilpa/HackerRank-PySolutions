# https://www.hackerrank.com/challenges/30-loops/problem

#!/bin/python3

import sys


n = int(input().strip())
for i in range(1, 11):
    print(str(n) +" x " + str(i) + " = " + str(n *i))