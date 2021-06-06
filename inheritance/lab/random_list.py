from random import choice


class RandomList(list):

    def get_random_element(self):
        element = choice(self)
        self.remove(element)
        return element

    # previous course and doesn't work
    # def get_random_element(self):
    #     element_index = randint(0, len(self) - 1)
    #     element = self[element_index]
    #     self.pop(element_index)
    #     return element

# test first zero
import unittest
from unittest import mock
import random

class RandomListTests(unittest.TestCase):
    def test_zero_first(self):
        mocked_choice = lambda x: 5
        with mock.patch('random.choice', mocked_choice):
            li = RandomList()
            li.append(4)
            li.append(3)
            li.append(5)
            self.assertEqual(li.get_random_element(), 5)

if __name__ == '__main__':
    unittest.main()

# rl = RandomList([1, 2, 3, 4])
# print(rl)
# rl.append(-1)
# print(rl)
# print(rl.get_random_element())
# print(rl)

