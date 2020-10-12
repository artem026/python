from time import time
from itertools import cycle


class TrafficLight:
    __color = 'Красный'

    def running(self):
        colors = cycle(['Красный', 'Желтый', 'Зеленый'])
        self.__color = next(colors)
        new_time = time()
        next_time = time()
        print(f' Светофор: {self.__color}')
        while time() < new_time + 100:
            # цикл в 100 сек
            if (time() > next_time + 7, time() > next_time + 2, time() > next_time + 15)[self.__color == 'Желтый']:
                next_time = time()
                self.__color = next(colors)
                print(f'Светофор: {self.__color}')


my_light = TrafficLight()
my_light.running()
