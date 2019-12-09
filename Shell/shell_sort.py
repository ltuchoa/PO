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


def sort(arr): 
    n = len(arr) 
    gap = n//2

    while gap > 0: 
  
        for i in range(gap,n): 

            temp = arr[i] 
            j = i 

            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            arr[j] = temp 
        gap //= 2

size = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    lista = generateList(s)
    time.append(timeit.timeit("sort({})".format(lista), setup="from __main__ import sort", number=1))
    print(s)

desenhaGrafico(size, time, "Size", "Time","Shell2.png")
print("FINISH")