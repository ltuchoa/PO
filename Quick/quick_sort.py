import timeit
from random import randint
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
    list = []
    while size:
        list.append(size)
        size -= 1
    return list


def quicksort(alist, start, end):
    if start < end:
        pIndex = partition(alist, start, end)
        quicksort(alist, start, pIndex-1)
        quicksort(alist, pIndex+1, end)


def partition(alist, start, end):
    pivot = randint(start, end)
    temp = alist[end]
    alist[end] = alist[pivot]
    alist[pivot] = temp
    pIndex = start

    for i in range(start, end):
        if alist[i] <= alist[end]:
            temp = alist[i]
            alist[i] = alist[pIndex]
            alist[pIndex] = temp
            pIndex += 1
    temp1 = alist[end]
    alist[end] = alist[pIndex]
    alist[pIndex] = temp1

    return pIndex


size = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    lista = generateList(s)
    time.append(timeit.timeit("quicksort({}, {}, {})".format(lista, 0, s - 1),
                              setup="from __main__ import quicksort", number=1))
    print(s)

desenhaGrafico(size, time, "Size", "Time", "Quick_Sort.png")
print("FINISH")
