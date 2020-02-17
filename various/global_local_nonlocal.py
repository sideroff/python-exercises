global_variable = 'global_variable_value'


# all variables can be read in a nested block
# but to modify them you need to specify an access
# modifier? global | nonlocal
# global accesses the global scope
# nonlocal accesses any of the parent scopes


def parent():
    local_variable = 'local_variable_value'
    print('''
    parent executed 
    global: {}, 
    local: {}
    '''.format(global_variable, local_variable))

    def first_child():
        global global_variable
        global_variable = 'first_child_changed_global'

        nonlocal local_variable
        local_variable = 'nonlocal_variable_value'

        first_child_local_variable = 'first_child_local_variable' 
        print('''
        first_child executed 
        global: {}, 
        local: {}
        '''.format(global_variable, local_variable))

        def second_child():
            nonlocal local_variable
            nonlocal first_child_local_variable
            print('''
            second_child executed 
            local_variable: {}
            first_child_local_variable: {}
            '''.format(local_variable, first_child_local_variable))
        
        second_child()
    
    first_child()
    print('''
    parent executed 
    global: {}, 
    local: {}
    '''.format(global_variable, local_variable))

    return first_child

parent()