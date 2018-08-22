"""
List of numbers that display the s min, max, sum and len.
"""
import math

def main():

    numbers = []
    for number in range(1, 5 + 1):
        number_entered = int(input("Number: "))
        numbers.append(number_entered)

    print_report(numbers)


def print_report(numbers):
    print("The first number is {} \nThe last number is {} \nThe largest number is {} "
          "\nThe average number is {}".format(numbers[0], numbers[-1], max(numbers), sum(numbers)/len(numbers)))


main()
