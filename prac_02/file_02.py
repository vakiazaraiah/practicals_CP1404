"""Create a text file called "numbers.txt" (You can create a simple text file in PyCharm with Ctrl+N, choose
"File" and save it in your project). Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens "numbers.txt", reads the numbers and adds them together then prints the result,
which should be... 59."""

# NUMBER_1 = 17
# NUMBER_2 = 42
# OUTPUT_FILE = 'numbers.txt'
#
# out_file = open(OUTPUT_FILE, 'w')
# print("{}\n{}".format(NUMBER_1, NUMBER_2), file=out_file)
# out_file.close()

out_file = open('numbers.txt', 'r')
number_1 = int(out_file.readline())
number_2 = int(out_file.readline())
print(number_2, number_1)
out_file.close()
