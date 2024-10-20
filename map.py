import numpy as np


class Map:
    def __init__(self):
        # перегородка в центре карты
        rock1_cords = np.array([[50, 50], [50, 49], [50, 51]])

        rock2_cords = np.array([[70, 10], [71, 10], [72, 10]])

        self.__rocks_cords = np.concatenate((rock1_cords, rock2_cords), axis=0)

    def get_rocks(self):
        return self.__rocks_cords


# class Rock:
#     def __init__(self, cords):
#         self.__cords = cords

#     def get_pos(self):
#         return self.__cords
