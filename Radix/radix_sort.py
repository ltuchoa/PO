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


def sort(list):
	exp = 1
	maxNumber = max(list)
 
	while maxNumber/exp > 0:
		ind = len(list) + 1
		count = [0] * ind
 
		for  i in list:
			count[i] += 1
 
		a = 0
		for i in range(ind):
			for j in range(count[0]):
				list[a] = i
				a += 1
 
		exp *= 10


size = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    print("START")
    lista = generateList(s)
    time.append(timeit.timeit("sort({})".format(lista),
                              setup="from __main__ import sort", number=1))
    print(s)

desenhaGrafico(size, time, "Size", "Time", "Radix_Sort.png")
print("FINISH")
