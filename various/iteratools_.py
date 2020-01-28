import re
import itertools

'''

HAWAII + IDAHO + IOWA's + OHIO = STATES


I + LOVE + YOU = DORA
SEND + MORE = MONEY
'''
# cryptarithms
lines = '''
HAWAII + IDAHO + IOWA's + OHIO = STATES
'''

word_pattern = '[\w\']+'
# Create a generator that yields any non-empty line mapped to uppercase
gen = (line.upper().replace("'", '') for line in lines.split('\n') if line)

# A generator that returns None (eg. when the generator is exhausted)
# will automatically raise a StopIteration Exception. This is then swallowed
# ( silently caught ) by the for loop since that's what it expects to receive
# when the generator is done.

# itertoos.groupby liniarly groups ( aka groups until a number that is not 
# part of the group appears ) eg. groupby [1,2,3,4,6,5,7] odd returns 
# 1,
# 2,
# 3,
# 4, 6,
# 5, 7


def get_gen(lines: str):
    split_lines = lines.split('\n')
    for line in split_lines:
        if not line:
            continue
        yield line.upper()
# gen = get_gen(lines)


f = open('itertools.txt','w+')

has_found_solution = False
for line in gen:
    
    has_found_solution = False
    words = re.findall(word_pattern, line)

    unique_chars = set(''.join(words))
    unique_chars_list = list(unique_chars)


    f.write('''
    Unique characters: {}
    len: {}
    {}
    '''.format(unique_chars, len(unique_chars), line))

    assert len(unique_chars) <= 10, 'Too many unique letters'

    first_chars = {word[0] for word in words}


    for perm in itertools.permutations(range(0,10), len(unique_chars)):
        guess = line.replace('=','==')
        has_failed = False
        for idx, num in enumerate(perm):
            if num == 0 and unique_chars_list[idx] in first_chars:
                has_failed = True
                break
            
            guess = guess.replace(unique_chars_list[idx], str(num))
        
        if has_failed: continue

        if eval(guess):
            has_found_solution = True
            f.write(guess.replace('==','=') + '\n')

if not has_found_solution:
    f.write('No solution found.\n')

# # Maps char with ascii code to str / char ascii
# translation_table = {
#     65: '1',
#     66: '2',
#     67: '3'
# }
# 'abc'.translate(translation_table)