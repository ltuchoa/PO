import timeit
from random import randint
import matplotlib.pyplot as plt


def desenhaGrafico(x, y1, y2, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y1, label="Aleatorio")
    ax.plot(x, y2, label="Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

def generateDList(size):
    list = []
    while size > 0:
        list.append(size)
        size -= 1
    return list

def generateList(size):
    list = []
    while size > 0:
        n = randint(1, size)
        if n not in list:
            list.append(n)
        size -= 1
    return list

op1 = []
op2 = []

def sort(array):
    operacoes = 0
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1
            operacoes += 1

        array[p] = current_element

    op1.append(operacoes)

def sort2(array):
    operacoes = 0
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1
            operacoes += 1

        array[p] = current_element

    op2.append(operacoes)

size = [10000, 20000, 50000, 100000]
time = []
timeD = []

for s in size:
    print(s)
    lista = generateList(s)
    listaD = generateDList(s)
    time.append(timeit.timeit("sort({})".format(lista),
                              setup="from __main__ import sort", number=1))
    timeD.append(timeit.timeit("sort2({})".format(listaD),
                               setup="from __main__ import sort2", number=1))


desenhaGrafico(size, time, timeD, "Size", "Time", "/Insertion_Sort.png")
desenhaGrafico(size, op1, op2, "Size", "Swaps", "Insertion_Sort_Swaps.png")
