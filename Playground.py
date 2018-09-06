

is_valid_input = False
while not is_valid_input:
    try:
        title = (input("Title: "))
        if title == '':
            print("Must not be blank")
        else:
            is_valid_input = True
    except ValueError:  # or just  except:
        print("Invalid (not an integer)")
print(title)

