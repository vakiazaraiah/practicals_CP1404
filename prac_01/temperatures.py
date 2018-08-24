"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = ask_for_input()
    while choice != "Q":
        choice = check_options(choice)
    print("Thank you.")


def check_options(choice):
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = converting_to_fahrenheit(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("fahrenheit:"))
        celsius = converting_to_celsius(fahrenheit)
        print("Result: {:.2f}".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = ask_for_input()
    return choice


def ask_for_input():
    choice = input(">>> ").upper()
    return choice


def converting_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def converting_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()
