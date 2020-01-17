# any function that has a yield statement will return a generator
def gen(x: int):
    print('making generator')
    for i in range(x):
        print('yielding')
        yield i
        print('after yield')


if __name__ == "__main__":
    counter = gen(5)

    print(next(counter))
    print(next(counter))
    # closing the generator will make any subsequent calls for next() throw an error
    # counter.close()
    print(next(counter))
    print(next(counter))
    print(next(counter))
