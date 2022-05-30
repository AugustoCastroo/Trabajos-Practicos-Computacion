hora = float(input("Ingrese la hora actual: "))
for hora in range(0, 23):
    if hora >= 20:
        print("Estamos en problemas", hora)
