roman_numeral_map = (
    ('M',  1000),
    ('CM', 900),
    ('D',  500),
    ('CD', 400),
    ('C',  100),
    ('XC', 90),
    ('L',  50),
    ('XL', 40),
    ('X',  10),
    ('IX', 9),
    ('V',  5),
    ('IV', 4),
    ('I',  1)
)

max_possible_integer = 3999

def to_roman(integer: int):
    '''convert integer to Roman numeral'''

    if type(integer) != int:
        raise TypeError('Porvided argument is not of type int')
    
    if integer <1 or integer > 3999:
        raise ValueError('Provided argument is not in the range (1, 3999)')

    result = ''

    for roman_numeral, integer_value in roman_numeral_map:
        while integer >= integer_value:
            result += roman_numeral
            integer -= integer_value
    
    return result

def from_roman(roman_numeral: str):
    '''convert Roman numeral to integer'''
    pass



# if __name__ == '__main__':
#     to_roman('asd')