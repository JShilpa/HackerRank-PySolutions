# Strings
# https://www.hackerrank.com/challenges/reduced-string/problem

def super_reduced_string(s):
    str_list = list(s)
    i = 0
    while i < len((str_list))-1:
        if str_list[i] == str_list[i+1]:
                del str_list[i]
                del str_list[i]
                i = 0
        else:
            i += 1
    if len(str_list) != 0:
        return ''.join(str_list)
    else:
        return 'Empty String'

s = input().strip()
result = super_reduced_string(s)
print(result)