class Papaya:
    '''Holds a papaya object and its age.'''

    has_roots = True

    def __init__(self, age: int):
        print('__init__ called')
        self.age = age

my_papaya = Papaya(5)
my_second_papaya = Papaya(6)

print('\nmy_papaya.age: {}\n'.format(my_papaya.age))


# Every instance has it's own set of static variables that can be overwritten,
# but won't affect any other instances. To do that, you must access the __class__.<var>
# And even then the instance static variable must not have been changed.
my_papaya.has_roots = 3
print('my_papaya.has_roots: {}'.format(my_papaya.has_roots))
print('my_second_papaya.has_roots: {}\n'.format(my_second_papaya.has_roots))

my_papaya.__class__.has_roots = False
print('my_papaya.has_roots: {}'.format(my_papaya.has_roots))
print('my_second_papaya.has_roots: {}\n'.format(my_second_papaya.has_roots))

print('Papaya.__doc__: {}'.format(my_papaya.__doc__))
print('Papaya.__class__: {}'.format(my_papaya.__class__))

class Fib:
    '''Fibonacci'''

    def __init__(self, max: int = 100):
        self.max = max
    
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    
    def __next__(self):
        fib = self.a
        
        if fib > self.max:
            raise StopIteration
        
        self.a, self.b = self.b, self.a + self.b
        
        return fib

for n in Fib(1000):
    print(n, end=' ')