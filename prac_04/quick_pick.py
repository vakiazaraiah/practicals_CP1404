
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program - choose sets of random numbers."""
    number_of_quick_picks = int(input("Quick picks? "))
    while number_of_quick_picks < 0:
        print("Please try again!")
        number_of_quick_picks = int(input("Quick picks? "))

    for i in range(number_of_quick_picks):
        quick_picks = []
        for l in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(",".join("{:3}".format(number) for number in quick_picks))


main()
# the following uses a generator expression (like a list comprehension)
        # to format each number in quick_picks in the same way
        # this is then turned into a single string with the join method