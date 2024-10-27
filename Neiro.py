from random import randint


class Neiro:
    def __init__(self,layer,number,weight,sm):  # создаем нейрон, задаем слой нейрона, вес и смещение
        self.__layer = layer
        self.__number = number
        self.__weight = weight
        self.__sm = sm
        self.__X = []
    
    def input(self,x):                          # принимаем значения с предыдущего слоя 
        self.__X.append(x)                      
    def send(self):                             # преобразовывем полученные числа и отправляем на следующий слой
        s = 0

        for i in range(len(self.__X)):
            s += self.__X[i]
        self.__X.clear()
        if (s*self.__weight + self.__sm)%3 == 1:
            return 1
        elif (s*self.__weight + self.__sm)%3 == 0:
            return 0
        else:
            return -1
class Neiro_S:
    def __init__(self,number_of_Neiros):      #создает нейросеть, 1 вход и 1 выход , середина - number_of_Neiros 
        self.__number = number_of_Neiros
        Neiros_ = []
        Neiros_.append(Neiro(0,0,1,0))
        for i in range(self.__number):
            Neiros_.append(Neiro(1,i,randint(0,100),randint(0,100)))
        Neiros_.append(Neiro(2,0,1,randint(0,100)))
        self.__N_S = Neiros_

    def step(self,input_coord):             #расчитывает шаг от коррдинаты передавая значения с первого нейнора на средние, со средних на последние
        self.__N_S[0].input(input_coord)
        for i in range(self.__number):
            self.__N_S[i+1].input(self.__N_S[0].send())
            self.__N_S[-1].input(self.__N_S[i+1].send())
        return self.__N_S[-1].send()
