from itertools import permutations


def possible_permutations(list_of_numbers):
    return (list(el) for el in permutations(list_of_numbers))


[print(n) for n in possible_permutations([1, 2, 3])]



# def possible_permutations(numbers):
#     if len(numbers) == 0:
#         return []
#     if len(numbers) == 1:
#         return [numbers]
#
#     permutations = []
#
#     for i in range(len(numbers)):
#         first_part = numbers[i]
#         numbers_remain = numbers[:i] + numbers[i + 1:]
#
#         for p in possible_permutations(numbers_remain):
#             permutations.append([first_part] + p)
#
#     return permutations
#
# [print(n) for n in possible_permutations([1, 2, 3])]


