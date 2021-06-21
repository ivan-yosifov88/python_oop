# def genrange(start, end):
#     return (num for num in range(start, end + 1))


def genrange(start, end):
    for num in range(start, end + 1):
        yield num

print(list(genrange(1, 10)))