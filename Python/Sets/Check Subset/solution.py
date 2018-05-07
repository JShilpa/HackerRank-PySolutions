# Sets Questions
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

for _ in range(int(input())):
    a, set_a = input(), set(map(int, input().split()))
    b, set_b = input(), set(map(int, input().split()))

    print(set_a.issubset(set_b))
