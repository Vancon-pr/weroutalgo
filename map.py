import numpy as np


class Map:
    def __init__(self):
        # перегородка в центре карты
        rock1_cords = np.array([[50, 50], [50, 49], [50, 51]])

        rock2_cords = np.array([[70, 10], [71, 10], [72, 10]])

        self.__rocks_cords = np.concatenate((rock1_cords, rock2_cords), axis=0)

        # Создание карты
        self.__map = np.zeros((100, 100))
        for i in range(100):
            for j in range(100):
                self.__map[i][j] = np.exp((i**2 + j**2) * 10e-4)

        # add rocks on map
        for i in range(len(self.__rocks_cords)):
            cord = self.__rocks_cords[i]
            self.__map[cord[0]][cord[1]] = 0

    def get_rocks(self):
        return self.__rocks_cords

    def get_map(self):
        return self.__map


# class Rock:
#     def __init__(self, cords):
#         self.__cords = cords

#     def get_pos(self):
#         return self.__cords
