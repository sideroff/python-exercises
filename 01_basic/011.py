import inspect

function = abs

full_args = inspect.getfullargspec(function)

print(function.__name__ + "(%s) -> " % ", ".join(full_args.args), full_args.annotations)
print(inspect.cleandoc(function.__doc__))
