"""Accountant Annie wants you to write a program to calculate the monthly cumulative totals for incomes.
The program should ask for the number of monthly incomes to enter, then get and store them in a list.
When the incomes have been entered, the program should display a list of the month's income next to the cumulative
income at that point - for each month. Here's some sample output:"""


def main():

    incomes = []
    number_of_months = int(input("How many months?"))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter incomes for month {}: ".format(month)))
        incomes.append(income)

    print_report(incomes)


def print_report(income):
    print("\nIncome Report\n----------")
    total = 0
    for month, income in enumerate(income):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month+1, income, total))


main()
