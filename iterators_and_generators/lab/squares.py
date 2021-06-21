# class squares:
#     def __init__(self, end):
#         self.end = end
#
#     def __iter__(self):
#         index = 1
#         while index <= self.end:
#             yield index * index
#             index += 1


# def squares(n):
#     return (num * num for num in range(1, n + 1))


def squares(n):
    index = 1
    while index <= n:
        yield index * index
        index += 1


print(list(squares(5)))