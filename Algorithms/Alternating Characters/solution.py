# Strings Problem
# https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    s = list(s)
    i = 0
    count = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            del (s[i])
            count += 1
        else:
            i += 1
    return count


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
