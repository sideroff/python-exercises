def is_vowel(char: str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    if len(string_input) > 1:
        print("More than 1 character received. Choosing the first char as default.")

    char = string_input[:1]

    print("Your char is a vowel" if char in vowels else "Your char is not a vowel")

string_input = input("Choose a char: ")

is_vowel(string_input)
