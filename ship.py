import numpy as np


class Ship:
    def __init__(self):
        # Инициализвация начального положения
        self.__cords = np.array([[0, 0]])

    def log(self):
        print(self.__cords)

    def calculate(self):
        # Получить информацию о препятствиях - через аргумент
        # Построить на её основе маршрут
        # Вернуть массив точек

        self.__cords = np.array([[i, i] for i in range(0, 101)])

        # за 1 шаг (1 сек) корабль перермещается на 1 клетку
        # __cords -- хранит информацию о всех шагах, полагая, что скорость
        # между двумя шагами проходит 1 секунда, тогда корабль
        # проходит диагональ единичного квадрата за секунду =>
        # на данный момент постоянная скорость = (sqrt(2) / 1) м/c
        return self.__cords

    def get_pos_at(self, step):
        return self.__cords[step]
