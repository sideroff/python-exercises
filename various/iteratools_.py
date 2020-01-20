import re

# cryptarithms 
lines = '''

HAWAII + IDAHO + IOWA's + OHIO = STATES


I + LOVE + YOU == DORA
SEND + MORE == MONEY
'''

word_pattern = '[\w\']+'
# Create a generator that yields any non-empty line mapped to uppercase
gen = (line.upper() for line in lines.split('\n') if line)

# A generator that returns None (eg. when the generator is exhausted)
# will automatically raise a StopIteration Exception. This is then swallowed
# ( silently caught ) by the for loop since that's what it expects to receive 
# when the generator is done.

def get_gen(lines: str):
    split_lines = lines.split('\n')
    for line in split_lines:
        if not line: continue
        yield line.upper()
# gen = get_gen(lines)

for line in gen:
    words = re.findall(word_pattern, line)
    
    unique_chars = set(''.join(words))

    assert len(unique_chars) <= 10, 'Too many unique letters'

    unicode_values_gen = (ord(c) for c in unique_chars)



    print(unique_chars)