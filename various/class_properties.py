# using property decorator is a different way to say the same thing
# as the property function

class Person:
    def __init__(self, name: str):
        self.__name = name

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    name = property(getname, setname)


class DifferentPerson:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


p = DifferentPerson('Steve')
# p = Person('Steve')

print(p.name)
p.name = 'Josh'
print(p.name)
