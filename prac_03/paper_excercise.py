"""Azaraiah Vaki"""

password = input("Enter password// ")

while len(password) < 4:
    print("Invalid passeword")
    password = input("Enter password// ")

for char in password:
    print("*", end='')