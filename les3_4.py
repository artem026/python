def my_func(x, y):
    return print(1 / x ** abs(y))

my_func(2, -3)

# 2 вариант доработать формулу
def my_func(x, y):
    i = 1
    z = 1 / x * abs(y)
    while i < y:
        i = i + 1
    z = 1 / z * abs(y)
    return print(z)

my_func(2, -3)

