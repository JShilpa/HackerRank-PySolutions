# Hash tables Problem
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

def ransom_note(magazine, ransom):
    magazine_dict = {}
    for i in magazine:
        if i in magazine_dict:
            magazine_dict[i] +=  1
        else:
            magazine_dict[i] = 1

    for i in ransom:
        if i in magazine_dict:
            if magazine_dict[i] == 0:
                return False
            else:
                magazine_dict[i] -= 1
        else:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = list(input().strip().split(' '))
ransom = list(input().split(' '))
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")