# Sets Intersection Operator
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


english_total, english_roll_no = int(input()), set(map(int, input().split()))
french_total, french_roll_no = int(input()), set(map(int, input().split()))


print(len(english_roll_no.intersection(french_roll_no)))