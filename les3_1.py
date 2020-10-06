def my_sum(num_1, num_2):
    while num_2 == 0:
        num_2 = int(input('Ввведите второе число : '))
    return num_1 / num_2

user_a = int(input('Ввведите первое число: '))
user_b = int(input('Ввведите второе число: '))
print(my_sum(user_a, user_b))

# 2 Вариант
def my_s(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на ноль!')
    except ValueError:
        print('Введено не число!')

a = int(input('Ввведите первое число: '))
b = int(input('Ввведите второе число: '))
print(my_s(a, b))
