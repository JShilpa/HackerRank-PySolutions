# https://www.hackerrank.com/challenges/30-review-loop/problem

n = int(input().strip())
for i in range(n):
    str = input()
    even_string = ''
    odd_string = ''
    for i in range(len(str)):
        if i % 2 == 0:
            even_string += str[i]
        else:
            odd_string += str[i]
    print(even_string + " " + odd_string)
