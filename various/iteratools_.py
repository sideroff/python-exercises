import re
import itertools

'''

HAWAII + IDAHO + IOWA's + OHIO = STATES


I + LOVE + YOU == DORA
SEND + MORE == MONEY
'''
# cryptarithms
lines = '''
AE + BE = CE
'''

word_pattern = '[\w\']+'
# Create a generator that yields any non-empty line mapped to uppercase
gen = (line.upper().replace("'", '') for line in lines.split('\n') if line)

# A generator that returns None (eg. when the generator is exhausted)
# will automatically raise a StopIteration Exception. This is then swallowed
# ( silently caught ) by the for loop since that's what it expects to receive
# when the generator is done.


def get_gen(lines: str):
    split_lines = lines.split('\n')
    for line in split_lines:
        if not line:
            continue
        yield line.upper()
# gen = get_gen(lines)



for line in gen:
    words = re.findall(word_pattern, line)

    unique_chars = set(''.join(words))
    unique_chars_list = list(unique_chars)

    print('''
    Unique characters: {}
    len: {}
    '''.format(unique_chars, len(unique_chars)))

    assert len(unique_chars) <= 10, 'Too many unique letters'

    first_chars = {word[0] for word in words}

    for perm in itertools.permutations(range(0,10), len(unique_chars)):
        for idx, num in enumerate(perm):
            if num == 0 and unique_chars_list[idx] in first_chars:
                print('skipping')
                break
            
            guess = line.replace('=', '==')
            for idx, char in enumerate(unique_chars_list):
                guess = guess.replace(char, str(perm[idx]))
            
            try:
                if(eval(guess)):
                    pass
                    # print(guess)
            except:
                print('''
                {}
                {}
                '''.format(unique_chars_list, perm))

    pass
    unicode_values_gen = (ord(c) for c in unique_chars)

    # print(unique_chars)
