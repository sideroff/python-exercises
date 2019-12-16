import sys

file_name = input("Sample filename : ")

split_file_name = file_name.split(".")

if len(split_file_name) == 1:
    print("File name does not contain an extension")
    sys.exit(0)

file_extension = file_name.split(".")[-1]
print("File extension : " + file_extension)