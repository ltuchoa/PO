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


def generateList(size):
    lista = list(range(1, size + 1))
    shuffle(lista)
    return lista


def sort(array, maxval):
    m = maxval + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for _ in range(count[a]):
            array[i] = a
            i += 1


size = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    lista = generateList(s)
    time.append(timeit.timeit("sort({}, {})".format(lista, max(lista)+1),
                              setup="from __main__ import sort", number=1))
    print(s)

desenhaGrafico(size, time, "Size", "Time", "Count_Sort.png")
print("FINISH")
