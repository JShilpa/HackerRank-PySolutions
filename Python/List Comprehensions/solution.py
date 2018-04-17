# List Comprehension Problem
# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x,y,z, n = [int(input()) for i in range(4)]
    print([[i,j,k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z+ 1) if(i + j + k) != n])


