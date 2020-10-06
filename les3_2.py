def next_list(name, surname, year, city, mail, tel):
    return print(name, surname, year, city, mail, tel)


next_list(name='Alex',
                surname='Good',
                year='2000',
                city= 'Moscow',
                mail= 'mail@mail.com',
                tel= '88001234567')

# 2 пользователь самостоятельно вводит данные

def next_list(**kwargs):
    return print(kwargs)


next_list(name=input('Введите имя:'),
                surname=input('Введите фамилию:'),
                year=input('Год рождения:'),
                city=input('Город:'),
                mail=input('email:'),
                tel=input('Телефон:'))

