# 1_Escribir un programa, para leer un archivo de texto completo.

class Lectura:
    def __init__(self, lectura):
        self.lectura = lectura

    def set_read(self):
        return self.lectura

    def read_text(self):
        file = open(self.lectura, "r")
        read = file.read()
        return read

with open(r"D:\Augusto\Computación Pycharm\tp3 Castro\texto.txt", "r"):
    print(Lectura.read_text())