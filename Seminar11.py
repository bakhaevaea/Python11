import matplotlib.pyplot as plt
import random

def Task1():
    # Постройте график функции
    # 𝑓 𝑥 = 5𝑥^2 + 10𝑥 − 30
    # По графику определите, при каких значения x значение функции отрицательно.
    x = [i for i in range(-5, 4)]
    func = [5*i*i + 10*i -30 for i in x]

    plt.plot(x, func)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title('f(x) = 5x^2 + 10x - 30')
    plt.grid(True) 
    plt.show()

def Task2():
    # Задача 2. Имеются данные о площади и стоимости 15 домов.
    # Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000
    # рублей.
    # Предоставьте ему графические данные о стоимость квадратного метра каждого дома и
    # список подходящих ему домов, отсортированных по площади.
    # Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров,
    # цены от 3 до 20 млн.

    house = [ (random.randint(100,301),random.randint(3000000, 20000001), f'дом {i+1}')for i in range(15)]
    # сортируем по площади
    house.sort(key = lambda x: x[0])
    square = []
    price_kv_m = []
    for i in range(15):
        a = int(round(house[i][1]/house[i][0], 0))
        if a < 50000:   # отбираем дома, стоимость квадратного метра которых < 50000
            square.append(str(house[i][2]) + " - " + str(house[i][0]))
            price_kv_m.append(a)

    plt.bar(square, price_kv_m)
    plt.title('Цены за кв.м')
    plt.xlabel('дома')
    plt.ylabel('цена кв.м')
    ax = plt.gca()
    plt.show()

Task2()