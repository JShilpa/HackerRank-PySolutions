# https://www.hackerrank.com/challenges/30-operators/problem
#!/bin/python3

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    tip = (tip_percent / 100) * meal_cost
    tax = (tax_percent / 100) * meal_cost
    total_cost = round(meal_cost + tip + tax)

    print("The total meal cost is " + str(total_cost) + " dollars.")



