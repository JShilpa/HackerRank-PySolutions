# Basic Data Type
# https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    students=[[input(), float(input())] for _ in range(int(input()))]
    c = sorted(set(grade for name,grade in students))[1]
    student_names =[name for name,grade in students if grade == c]
    print('\n'.join(sorted(student_names)))
