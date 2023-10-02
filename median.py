"""Median calculator."""
import math

"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers = sorted(numbers)

if len(numbers)%2 == 0:
    middlePoint = int(len(numbers)/2) - 1
    median = (numbers[middlePoint] + numbers[middlePoint+1])/2
else:
    middlePoint = math.floor(len(numbers)/2)
    median = numbers[middlePoint]

print(median)

