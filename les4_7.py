# не работает
def fact(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x
n = int(input('Введите число'))
for el in fact(n):
    print(n)
