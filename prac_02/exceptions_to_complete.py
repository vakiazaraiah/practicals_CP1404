"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
"""Let's write a program that gets an integer from the user and does not crash '
   'when a non-number is entered."""
finished = False
result = 0

while not finished:
    try:
        # TODO: this line
        result = int(input("Please enter a Number: "))
        # TODO: this line
        finished = True
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")

print("Valid result is:", result)

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     if numerator == 0 or denominator == 0:
#         print("Numerator and denominator must be valid numbers!")
#     else:
#         fraction = numerator / denominator
#         print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# print("Finished.")