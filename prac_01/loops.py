for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

maximum_number_of_stars = int(input("Please enter a number"))
star = '*'
for number_of_stars in range(1, 1 + maximum_number_of_stars):
    print('{}'.format(star * number_of_stars))

