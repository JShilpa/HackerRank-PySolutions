# Sets Question
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem




m, english = input(), set(map(int,input.split()))
n, french = input(), set(map(int,input.split()))

print(len(english.symmetric_difference(french)))
