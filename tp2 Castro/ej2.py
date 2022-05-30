import os
import re

path = (r"D:\Augusto\Pycharm\PyCharm Community Edition 2021.2\PycharmProjects\pythonProject1\tp2 Castro\secretkey")
path1 = (r"D:\Augusto\Pycharm\PyCharm Community Edition 2021.2\PycharmProjects\pythonProject1\tp2 Castro\Nuevo secretkey")

file = os.listdir(path)

lista = []
lista2 = []

for x in file:
    nuevo = re.sub(r"^\d", "", x)
    lista.append(nuevo)
for i in lista:
    nuevo = re.sub(r"^\d", "", i)
    lista2.append(nuevo)

os.chdir(r"D:\Augusto\Pycharm\PyCharm Community Edition 2021.2\PycharmProjects\pythonProject1\tp2 Castro\secretkey")
for y, z in zip(os.listdir(), lista2):
    os.replace(y, z)

print(lista2)