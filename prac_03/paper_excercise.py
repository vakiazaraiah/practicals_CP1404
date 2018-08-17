"""Azaraiah Vaki"""


def main():
    password = get_password()
    checking_character(password)
    main()


def checking_character(password):
    for character in password:
        print("*", end='')


def get_password():
    password = input("Enter password// ")
    while len(password) < 4:
        print("Invalid password")
        password = input("Enter password// ")
    return password

