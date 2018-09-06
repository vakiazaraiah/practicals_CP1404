"""
Testing out the guitar class.

"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2018

def run_tests():
    name = 'Gibson L-5 CES'
    year = 1922
    cost = 1635.40

    guitar = Guitar(name, year, cost)

    print("{} get_age() - Expected {}. Got {}, ${}".format(guitar.name, 96, guitar.get_age(),guitar.cost))

if __name__ == "__main__":
    run_tests()