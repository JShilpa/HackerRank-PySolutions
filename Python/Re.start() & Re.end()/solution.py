# Regex and Parsing
# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re





# s = input()
# k = input()
# flag = False

s ='aaadaa'
k ='aa'
flag = True

for i in s:
     m = re.search(k,s)
     print(m.start())
     print(m.end())


