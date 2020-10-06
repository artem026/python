def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(a, b, c))
    return print(sum(numbers))

my_func(1, 2, 3)
