"""The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
screen. The output should look something like (bold text represents user input):"""

items = int(input("Number of items:"))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Please enter the number of items:"))

total = 0
for i in range(items):
    price = float(input("Price of item:"))
    total += price

if total >= 100:
    discount = total * 0.10
    total = total - discount

print("Total price for", items, "items is $", total)
