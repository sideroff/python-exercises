input_text = input('Enter text: ')

if len(input_text) > 10:
    input_text = input_text[:9] + '...'

print(input_text)