from sys import path
# 

# by creating a __init__.py file in any dir you tell python that that dir is a package
# this allows you to use the . syntax you see below when importing
from package_example.custommodule import ANY_VAR


print(ANY_VAR)

# uncommenting this line will change python's directory check order and it will find ./folder/testmodule.py
# path.insert(0, './folder')
# from testmodule import test
# test()

