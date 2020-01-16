def args(*args):
    for arg in args:
        print('argument:', arg)


def kwargs(**kwargs):
    for k, v in kwargs.items():
        print('argument {}: {}'.format(k, v))


def both(*args, **kwargs):
    '''
        Uses both args and kwargs. 
    '''
    
    for arg in args:
        print('positional argument:', arg)
    for k, v in kwargs.items():
        print('named argument {}: {}'.format(k, v))

def with_mandatory(test: )

def main():
    # args(1, 2, 3, 4, 5, 6, 7, 8, 9)

    # kwargs(name='ivan', age=23)

    data = [1, 2, 3, 4, 5]
    # args(*data)

    person = {
        'name': 'ivan',
        'age': 23
    }
    # kwargs(**person)


    both(*data, **person)

if (__name__ == '__main__'):
    main()
