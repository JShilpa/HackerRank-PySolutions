# Basic Data Type Problem
# https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = input()
    student_score = student_marks[query_name]
    print("%.2f" %(sum(student_score)/len(student_score)))
