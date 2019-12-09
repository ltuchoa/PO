import timeit
from random import randint, shuffle
import matplotlib.pyplot as plt


def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def generatelista(size):
    lista = list(range(1, size + 1))
    shuffle(lista)
    return lista


def gnome_sort(lista):
    size = len(lista)
    index = 0
    while index < size:
        if index == 0:
            index = index + 1
        if lista[index] >= lista[index - 1]:
            index = index + 1
        else:
            aux = lista[index]
            lista[index] = lista[index-1]
            lista[index-1] = aux
            index = index - 1
    return lista


size = [10000, 20000, 30000, 40000, 50000, 100000]
time = []

for s in size:
    print("START")
    lista = generatelista(s)
    time.append(timeit.timeit("gnome_sort({})".format(lista),
                              setup="from __main__ import gnome_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Size", "Time",
               "/Users/LTUCH/Desktop/Gnome_Sort.png")
print("FINISH")
