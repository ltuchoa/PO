import timeit
from random import randint, shuffle
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10**6)


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


def sort(list):
    if len(list) > 1:
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]

        sort(L)
        sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1


size = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    lista = generateList(s)
    time.append(timeit.timeit("sort({})".format(lista),
                              setup="from __main__ import sort", number=1))
    print(s)

desenhaGrafico(size, time, "Size", "Time", "Merge_Sort2.png")
print("FINISH")
