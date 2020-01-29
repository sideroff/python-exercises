

class Withable():
    openned = False

    def __init__(self):
        print('constructor called, self.openned = {}'.format(self.openned))

    # should return self if you intend to use aliases:
    # with x as y
    #        ^               
    def __enter__(self):
        self.openned = True
        print('enter called, self.openned = {}'.format(self.openned))

        return self
    
    # python will be sure to call __exit__ once your code goes out of the block
    # no matter the cause
    def __exit__(self, etype, value, traceback):
        self.openned = False
        print('''exit called,
        self.openned = {},
        etype = {},
        value = {},
        traceback = {},
        '''.format(self.openned, etype, value, traceback))


withable_object = Withable()
print('1 withable_object.openned = {}'.format(withable_object.openned))

with withable_object:
    raise Exception('test')

    print('2 withable_object.openned = {}'.format(withable_object.openned))


print('3 withable_object.openned = {}'.format(withable_object.openned))
