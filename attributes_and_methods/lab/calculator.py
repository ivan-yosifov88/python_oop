class Calculator:

    @staticmethod
    def add(first_element, *args):
        result = first_element
        for el in args:
            result += el
        return result

    @staticmethod
    def multiply(first_element, *args):
        result = first_element
        for el in args:
            result *= el
        return result

    @staticmethod
    def divide(first_element, *args):
        result = first_element
        for el in args:
            result /= el
        return result

    @staticmethod
    def subtract(first_element, *args):
        result = first_element
        for el in args:
            result -= el
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
