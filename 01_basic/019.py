new_string = input("Choose a string: ")

if (not new_string.lower().startswith("is")):
    new_string = "Is %s" % new_string

print(new_string)