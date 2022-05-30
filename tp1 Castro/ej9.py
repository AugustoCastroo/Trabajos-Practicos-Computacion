cadena = str(input("Ingrese una palabra o frase: "))

def cadena_no(word):
    word1 = ""
    if str(word[0: 2]) != "no":
        word1 = "no " + "" + word
        print(word1)
    else:
        print(word)
cadena_no(cadena)