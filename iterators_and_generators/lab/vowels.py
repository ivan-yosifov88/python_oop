class vowels:

    vowels_set = {
        'a', 'e', 'y', 'u', 'i', 'o',
        'A', 'E', 'Y', 'U', 'I', 'O'
    }

    def __init__(self, text):
        self.text = text
        self.start = 0
        self.end = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.end < self.start:
            raise StopIteration
        index = self.start
        self.start += 1
        char = self.text[index]
        if not self.is_vowel(char):
            return self.__next__()
        return char


    @staticmethod
    def is_vowel(char):
        return char in vowels.vowels_set


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
