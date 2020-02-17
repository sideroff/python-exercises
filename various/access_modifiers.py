class Person:
    def __init__(self):
        print('Person constructor called')
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'

class ExtendedPerson(Person):
    def __init__(self):
        print('ExtendedPerson constructor called')
        super().__init__()
    


p = ExtendedPerson()
breakpoint()
print(p.public)
print(p._protected)
print(p.__private)
