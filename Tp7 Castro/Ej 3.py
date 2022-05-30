import random


def faltante(list):
    list.sort()
    return [x for x in range(list[0], list[-1] + 1) if x not in list]

list = list(range(0, 101))
random.shuffle(list)
list.remove(5)
print(list)
faltante(list)
print('El número que falta en la lista es:',faltante(list))