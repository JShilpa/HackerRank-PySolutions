# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def recursive_bubble_sort(arr, steps=None, swapped_count=None):
    if steps is None:
        steps = 0
    if swapped_count is None:
        swapped_count = 0
    swapped = False

    n = len(arr)
    if n is 1:
        return False

    for i in range(n - steps - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped_count += 1
            swapped = True

    if swapped is True:
        steps += 1
        recursive_bubble_sort(arr, steps, swapped_count)
    else:
        print("Array is sorted in " + str(swapped_count) + " swaps.")
        print('First Element: ' + str(arr[0]))
        print('Last Element: ' + str(arr[n - 1]))


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
recursive_bubble_sort(a)
