
out_file = open('name.txt','w')
user_name = input("Please enter your name// ")
print("Your name is {}".format(user_name), file=out_file)
out_file.close()
out_file = open('name.txt', 'r')
print(out_file.readline())
out_file.close()
