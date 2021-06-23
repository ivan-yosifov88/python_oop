from functools import wraps


def type_check(type_of_parameter):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for el in args:
                if not type(el) == type_of_parameter:
                    return "Bad Type"
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
