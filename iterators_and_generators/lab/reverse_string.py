def reverse_text(text):
    end = len(text) - 1
    for i in range(end, - 1, - 1):
        yield text[i]


for char in reverse_text("step"):
    print(char, end='')
