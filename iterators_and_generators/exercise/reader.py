def get_list_or_tuple_elements(argument):
    result = ''
    for el in argument:
        if type(el) is list:
            result += str(el[0])
        else:
            result += str(el)

    return result


def get_string_elements(argument):
    return argument.split()[0]


def get_dict_elements(argument):
    return ''.join(list(argument.keys()))


def get_tuple_elements(argument):
    return str(argument[0])


def get_argument(argument):
    result = None
    if type(argument) is list or type(argument) is tuple:
        result = get_list_or_tuple_elements(argument)
    elif type(argument) is str:
        result = get_string_elements(argument)
    elif type(argument) is dict:
        result = get_dict_elements(argument)

    return result


def read_next(*args):
    for arg in args:
        element = get_argument(arg)
        yield element


for item in read_next('string', (2, ), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
