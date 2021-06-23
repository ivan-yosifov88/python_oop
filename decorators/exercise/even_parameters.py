import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        even_numbers = []
        for el in args:
            try:
                if el % 2 == 0:
                    even_numbers.append(el)
            except TypeError:
                pass
        if len(even_numbers) == len(args):
            return func(*args, **kwargs)
        return "Please use only even numbers!"


    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
