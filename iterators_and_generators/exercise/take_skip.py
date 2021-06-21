class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.count:
            raise StopIteration
        number = self.number
        self.number += self.step
        self.index += 1
        return number


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

