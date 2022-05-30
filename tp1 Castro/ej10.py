word = str(input("Ingrese una palabra: "))
num = int(input("Ingrese un índice: "))

def caracter_perdido(str, a):
    if a == 0:
        mid1 = str[:a]
        mid2 = str[a+1:]
        return mid1 + mid2
    elif a == 1:
        return str[:-1]
    print(caracter_perdido(word, num))