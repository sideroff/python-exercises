

def parent(msg, flag: bool):
    local_variable = '15'
    print('parent executed {}'.format(msg))


    def first_child():
        print('first_child {}'.format(msg))

    
    def second_child():
        print('first_child {}, {}'.format(msg, local_variable))

    return (
        first_child if flag 
        else second_child
    )
    

global_variable = parent('testing', True)
print('-----')
global_variable()