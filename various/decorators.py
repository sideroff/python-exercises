def display_decorator(fn):
    def decorator(text):
        print('Output: ', end=' ')
        fn(text)
    return decorator


# adding this basically calls the function with the same name
# with the next lines function as an argument
@display_decorator
def display(text):
    print(text)

# my_decorator = display_decorator(display)

display('Hello World')