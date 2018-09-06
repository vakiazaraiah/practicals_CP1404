"""
Class for storing guitars.
"""

CURRENTYEAR = 2018


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.f2}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENTYEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50

