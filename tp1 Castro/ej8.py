a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

if a > 0 and b < 0:
    print("El número ", a, "es positivo, y el número", b, "es negativo")
elif a < 0 and b > 0:
    print("El número ", b, "es positivo, y el número", a, "es negativo")
elif a < 0 and b < 0:
    print("Ambos números son negativos")
else:
    print("Ambos números son positivos")
