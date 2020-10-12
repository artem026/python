class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def value(self, weight, height):
        print(f'Потребуется {self._length * self._width * weight * height} кг асфальта')


new_road = Road(20, 5000)
new_road.value(25, 5)
