from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args):
        name = function.__name__
        result = function(*args)
        return f"you called {name}{args}\nit returned {result}"
    return wrapper



@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
