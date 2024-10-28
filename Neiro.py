from random import randint


class Neiro:
    def __init__(self,layer,number,weight,sm):  # создает нейрон, задаем слой нейрона, вес и смещение
        self.__layer = layer
        self.__number = number
        self.__weight = weight
        self.__sm = sm
        self.__X = []
    
    def get_gen(self):                          #получает ген нейрона
        return([self.__weight,self.__sm])
    
    def set_gen(self,Gen):                      #устанавливает ген нейрона
        self.__weight = Gen[0]
        self.__sm = Gen[1]

    def input(self,x):                          # принимает значения с предыдущего слоя 
        self.__X.append(x)

    def send(self):                             # преобразовывет полученные числа и отправляет на следующий слой
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
    
    def get_genom(self):                    #получает геном данной сети
        Genom = []
        for i in range(1,len(self.__N_S)):
            Genom.append(self.__N_S[i].get_gen())
        return Genom
    def set_genom(self,Genom):              #устанавливает геном для данной сети
        for i in range(len(Genom)):
            self.__N_S[i+1].set_gen(Genom[i])

def mutation(U_genom):                      #создает мутации в U_genom
    for i in range(randint(0,len(U_genom)-1)):
        U_genom[i] = [randint(0,100),randint(0,100)]
    return U_genom 

def evolution(Neiros_1,Neirps_2):           #скрещивает двух сущностей класса Neiro_s, пока без мутаций
    U_genom = Neiros_1.get_genom()+Neirps_2.get_genom()
    new_geno_1 = []
    new_geno_2 = []
    i = 0
    U_genom = mutation(U_genom)
    while i < len(Neiros_1.get_genom()):
        i+= 1
        elem = randint(0,len(U_genom)-1)
        new_geno_1.append(U_genom.pop(elem))
    for i in range(len(U_genom)):
        new_geno_2.append(U_genom[i].copy())
    Neiros_1.set_genom(new_geno_1)
    Neirps_2.set_genom(new_geno_2)
