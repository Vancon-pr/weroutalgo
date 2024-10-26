import numpy as np
import time


class Ship:
    def __init__(self):
        # Инициализвация начального положения
        self.__cords = np.array([[0, 0]])

    def log(self):
        print(self.__cords)

    def calculate(self, map):
        # Получить информацию о препятствиях - через аргумент
        # Построить на её основе маршрут
        # Вернуть массив точек

        # self.__cords = np.array([[i, i] for i in range(0, 101)])
        x = 0
        y = 0
        while True:
            bot_coef = map[x][y - 1] if y != 0 else 0
            top_coef = map[x][y + 1] if y != 99 else 0
            right_coef = map[x + 1][y] if x != 99 else 0
            left_coef = map[x - 1][y] if x != 0 else 0

            lb_coef = map[x - 1][y - 1] if x != 0 and y != 0 else 0
            rb_coef = map[x + 1][y - 1] if x != 99 and y != 0 else 0

            lt_coef = map[x - 1][y + 1] if x != 0 and y != 99 else 0
            rt_coef = map[x + 1][y + 1] if x != 99 and y != 99 else 0

            variables = {
                "top_coef": top_coef,
                "bot_coef": bot_coef,
                "right_coef": right_coef,
                "left_coef": left_coef,
                "lb_coef": lb_coef,
                "rb_coef": rb_coef,
                "lt_coef": lt_coef,
                "rt_coef": rt_coef,
            }
            max_variable = max(variables, key=variables.get)
            if max_variable == "top_coef":
                y += 1
            elif max_variable == "bot_coef":
                y -= 1
            elif max_variable == "right_coef":
                x += 1
            elif max_variable == "left_coef":
                x -= 1
            elif max_variable == "lb_coef":
                x -= 1
                y -= 1
            elif max_variable == "rb_coef":
                x += 1
                y -= 1
            elif max_variable == "lt_coef":
                x -= 1
                y += 1
            elif max_variable == "rt_coef":
                x += 1
                y += 1
            if x == 99 and y == 99:
                break
            # print(right_coef, top_coef, max_variable)
            print(x, y)
            # time.sleep(1)

        # за 1 шаг (1 сек) корабль перермещается на 1 клетку
        # __cords -- хранит информацию о всех шагах, полагая, что скорость
        # между двумя шагами проходит 1 секунда, тогда корабль
        # проходит диагональ единичного квадрата за секунду =>
        # на данный момент постоянная скорость = (sqrt(2) / 1) м/c
        return self.__cords

    def get_pos_at(self, step):
        return self.__cords[step]
