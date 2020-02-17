# python won't call super().__init__ for you.
class Person:
    def __init__(self):
        print('Person constructor called')
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'

class ExtendedPerson(Person):
    def __init__(self):
        print('ExtendedPerson constructor called')
        # super().__init__()

# only ExtendedPerson is initialized =>
p = ExtendedPerson()
# the property on the parent class has not been initialized yet
print(p.public)


p = ExtendedPerson

