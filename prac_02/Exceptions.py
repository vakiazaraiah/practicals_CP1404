"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- The a character or float variable has been input.
2. When will a ZeroDivisionError occur?
- When the input for the denominator and numerator are equal to 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if numerator == 0 or denominator == 0:
        print("Numerator and denominator must be valid numbers!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
