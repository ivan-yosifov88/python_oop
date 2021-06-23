from functools import wraps

def vowel_filter(func):

    @wraps(func)
    def wrapper():
        vowel_letters = []
        vowels = {
            'a', 'e', 'u', 'i', 'o'
            'A', 'E', 'U', 'I', 'O'
        }
        for l in func():
            if l in vowels:
                vowel_letters.append(l)
        return vowel_letters
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
