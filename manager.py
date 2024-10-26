import time
import numpy as np
from ship import Ship
from map import Map


class Manager:
    def __init__(self):
        # количество кадров в сек
        self.__tick = 1 / 30

        self.__ship = Ship()
        self.__map = Map()

    def check_is_dead(self, pos):
        # Проверка есть ли точка pos в массиве с координатами скал
        if np.any(np.all(self.__map.get_rocks() == pos, axis=1)):
            return True
        return False

    def run(self):
        trajectory = self.__ship.calculate(self.__map.get_map())

        # i -- счётчик времени 1 шаг в "1 секунду в секунду"
        for i in range(len(trajectory)):
            pos = self.__ship.get_pos_at(i)

            if self.check_is_dead(pos):
                print(f"Крушение в {pos}")
                break

            # Печать перемещения корабля из (0,0) в (100,100))
            print(f'{" " * pos[0]}.')

            time.sleep(self.__tick)
