raw_data = input("Sample data : ")

split_data = raw_data.split(", ")

data_list = list(split_data)
data_tuple = tuple(split_data)

print("List : ", data_list)
print("Tuple : ", data_tuple)