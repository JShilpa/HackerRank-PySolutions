# Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    distinct_height = set(array)
    return sum(distinct_height) / len(distinct_height)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
