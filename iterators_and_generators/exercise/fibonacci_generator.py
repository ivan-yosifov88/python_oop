def fibonacci():
    number = 0
    previous_number = 1
    while True:
        if number == 0:
            yield number
            number += previous_number
        if number == 1:
            yield number
            number += previous_number
        if number == 2:
            yield previous_number
        if number > 1:
            yield number
            cutternt_number = previous_number
            previous_number = number
            number = cutternt_number + previous_number



generator = fibonacci()
for i in range(5):
    print(next(generator))




