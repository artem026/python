class Cell:

    def __init__(self, num):
        try:
            if num <= 0:
                raise ValueError('Ошибка.Значение меньше или равно 0')
            self.num = int(num)
        except TypeError:
            self.num = 1
            print('Ошибочные данные')
        except ValueError:
            print('Ошибочные данные')
            self.num = 1

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print('Операция вычитания невозможна')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.num // param) + '*' * (self.num % param)


cell_1 = Cell(12)
cell_2 = Cell(15)
print(cell_1.make_order(5))
print(cell_2.make_order(5))
