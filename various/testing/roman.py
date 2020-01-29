import re

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

roman_numeral_pattern = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)



def to_roman(integer: int):
    '''convert integer to Roman numeral'''

    if type(integer) != int:
        raise TypeError('Porvided argument is not of type int')

    # 1-3999 both inclusive
    if not 0 < integer < 4000:
        raise ValueError(
            'Provided argument is not in the range (1, 3999) both inclusive')

    result = ''

    for roman_numeral, integer_value in roman_numeral_map:
        while integer >= integer_value:
            result += roman_numeral
            integer -= integer_value

    return result


def from_roman(roman_numeral: str):
    '''convert Roman numeral to integer'''

    if type(roman_numeral) != str:
        raise TypeError('Porvided argument is not of type int')

    if not roman_numeral_pattern.search(roman_numeral):
        raise ValueError('Invalid Roman numeral: {}'.format(roman_numeral))

    result = 0
    index = 0

    for numeral, integer in roman_numeral_map:
        while roman_numeral[index: index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    
    return result


# if __name__ == '__main__':
#     to_roman('asd')
