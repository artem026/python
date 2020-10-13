class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше устан. для городского авто'
        else:
            return f'Скорость {self.name} соотв. разрешенной для городского авто'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше установленной для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не является полицейским авто'


bmw = SportCar(100, 'Черный', 'BMW', False)
mazda = TownCar(50, 'Красный', 'Mazda', False)
opel = WorkCar(80, 'Желтый', 'Opel', False)
oktavia = PoliceCar(150, 'Бело-синяя',  'Oktavia', True)

print(opel.turn_right())
print(f'{bmw.turn_left()}, а {mazda.stop()}')
print(f'{opel.go()} со {opel.show_speed()}')
print(f'У {opel.name} цвет {opel.color}')
print(f'{bmw.name} полицейский авто? {bmw.is_police}')
print(f'{oktavia.name} полицейский авто? {oktavia.is_police}')
print(bmw.show_speed())
print(mazda.show_speed())
print(oktavia.police())
print(oktavia.show_speed())
