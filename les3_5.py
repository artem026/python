def my_func():
    my_sum = 0
    while True:
        numbers = input('Введите числа через пробел или q для выхода:').split()
        for i in numbers:
            try:
                if i == 'q':
                    print(f'Подсчет завершен. Сумма равна: {my_sum}')
                    return
                else:
                    my_sum += int(i)
            except ValueError:
                print('Введите число или q для выхода')
        print(f'Сумма чисел равна: {my_sum}')

my_func()
