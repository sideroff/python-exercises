from sys import getsizeof


class Planet:
    def __init__(self, cities, rivers):
        self.cities = cities
        self.rivers = rivers


class SlottedPlanet:
    __slots__ = ['cities', 'rivers']

    def __init__(self, cities, rivers):
        self.cities = cities
        self.rivers = rivers


earth = Planet(['Sofia, London'], ['Danube', 'Thames'])


slotted_earth = SlottedPlanet(['Sofia, London'], ['Danube', 'Thames'])


size_of_object = getsizeof(earth)
size_of_object_props = getsizeof(earth.__dict__)

print(f'''
Normal object size = {size_of_object} + {size_of_object_props} = {size_of_object + size_of_object_props }
''')
