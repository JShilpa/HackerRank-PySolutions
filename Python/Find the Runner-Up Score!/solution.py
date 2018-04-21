# Basic Data Type Problem
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    print(sorted(arr)[-2])
