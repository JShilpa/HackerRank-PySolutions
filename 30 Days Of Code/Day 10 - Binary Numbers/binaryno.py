# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import sys

def generate_binary(no):
    binary_string = '0' if no % 2 == 0 else '1'
    no = no // 2
    while no != 0:
         if no % 2 == 0:
           binary_string += '0'
           no = no // 2
         else:
            binary_string += '1'
            no = no // 2
    return binary_string



n = int(input().strip())
count = len(max(generate_binary(n).split('0')))
print(count)



