from os import path

input_path = input("Choose filename: ")

print("File exists in current directory: %s" % path.exists(input_path))