import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import timeit
mpl.use('Agg')

def desenhaGrafico(x, y, nome, xl="Entradas", yl="Saídas"):
    plt.plot(x, y, label="Melhor Tempo")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nome)

def generateList(size):
    list = []
    while size > 0:
        n = randint(1, size)
        list.append(n)
        size -= 1
    return list

def generateDList(size):
    list = []
    while size > 0:
        list.append(size)
        size -= 1
    return list

op = []

def sort(array):
    operacoes = 0
    for final in range(len(array), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                array[current + 1], array[current] = array[current], array[current + 1]
                operacoes += 1
                exchanging = True

        if not exchanging:
            break

    op.append(operacoes)

size = [10000, 20000, 50000, 100000]
time = []

for s in size:
    list = generateList(s)
    time.append(timeit.timeit("sort({})".format(list),setup="from __main__ import sort", number=1))
    print(s)

desenhaGrafico(size, time,'Bolha_Tempo', "Numbers", "Time")
desenhaGrafico(size, op,'Bolha_Op', "Numbers", "Operations")
