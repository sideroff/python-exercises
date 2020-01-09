input_text = input('Enter text: ')
input_text2 = input('Enter text2: ')

index = input_text.find(input_text2)

print(input_text if index == -1 else input_text[index + len(input_text2):])
