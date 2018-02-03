# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input().strip())
phonebook = {}
for i in range(n):
    details = [temp_string for temp_string in input().split(' ')]
    phonebook[details[0].lower()] = details[1]
input_flag = True

while(input_flag):
    key = input().strip().lower()
    if key in phonebook:
        print(key + "=" + phonebook[key])
    else:
        print("Not found")

