# Sets Symmetric Difference Problem
# https://www.hackerrank.com/challenges/symmetric-difference/problem




len_m, m = input(), set(map(int, input().split()))
len_n, n = input(), set(map(int, input().split()))

print(*sorted((m.symmetric_difference(n))), sep='\n')