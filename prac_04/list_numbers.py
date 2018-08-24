"""
List of numbers that display the s min, max, sum and len.
"""
import math

def main():

    numbers = check_numbers()
    print_report(numbers)


def check_numbers():
    numbers = []
    for number in range(1, 5 + 1):
        number_entered = int(input("Number: "))
        numbers.append(number_entered)
    return numbers


def print_report(numbers):
    print("The first number is {} \nThe last number is {} \nThe largest number is {} "
          "\nThe average number is {}".format(numbers[0], numbers[-1], max(numbers), sum(numbers)/len(numbers)))


main()
