from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        try:
            float(param)
        except ValueError:
            print('Ошибочные данные')

    @abstractmethod
    def get_square(self):
        pass


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param=param)
        self.size = float(param)

    @property
    def get_square(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param=param)
        self.height = float(param)

    @property
    def get_square(self):
        return round(self.height * 2 + 0.3, 2)


my_coat = Coat(50)
my_suit = Suit(1.80)
print(f'Для создания пальто размера {my_coat.size} расход ткани составит: {my_coat.get_square}')
print(f'Для создания костюма роста {my_suit.height} расход ткани составит: {my_suit.get_square}')
print(f'Общий расход ткани составит: {my_coat.get_square + my_suit.get_square}')
