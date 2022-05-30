lista = [1, 2, 10]
diferencia = sorted (lista, reverse=True)


def array(diferencia):
    b = []
    for i in range(len(diferencia) - 1):
        b.append(diferencia[i] - diferencia[i + 1])
    print("Diferencia: ", b)

    def suma(b):
        suma = 0
        for numero in b:
            suma += numero
        return suma
    print("Sumatoria: ", suma(b))

print('Lista: ', lista)
print('Orden descendiente: ', diferencia)
array(diferencia)