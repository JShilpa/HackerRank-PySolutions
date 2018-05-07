# Sets Questions
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem


m, english = input(), set(map(int, input().split()))
n, french = input(), set(map(int, input().split()))

print(len(english.difference(french)))
