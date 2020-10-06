def calc():
    time = float(input('Количество отработанных часов: '))
    price = float(input('Стоимость часа работы: '))
    money = float(input('Размер премии: '))
    cash = time * price
    return cash + money
print(f'Итого: {calc()}')
