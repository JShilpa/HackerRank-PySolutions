# Sets Problem
# https://www.hackerrank.com/challenges/no-idea/problem

def compute_happiness(arr, set_a, set_b):
    happiness_count = 0
    for i in arr:
            if i in set_a:
                happiness_count += 1
            elif i in set_b:
                happiness_count -= 1

    print( happiness_count)

n, m = input().split()
nos = list(map(int, input().split()))
set_a = set(map(int,input().split()))
set_b = set(map(int,input().split()))
compute_happiness(nos,set_a,set_b)
