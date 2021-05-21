def generate_line(symbol, offset_space, symbol_count):
    offset = " " * offset_space
    content = ' '.join(symbol_count * f"{symbol}")
    return f"{offset}{content}"


def draw_line(symbol, offset_space, symbol_count):
    print(generate_line(symbol, offset_space, symbol_count))


def draw_rhombus(size):
    for i in range(1, size + 1):
        draw_line("*", size - i, i)

    for j in range(size - 1, 0, - 1):
        draw_line("*", size - j, j)


draw_rhombus(int(input()))
