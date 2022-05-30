lista_son = ["sonriendo"]
lista_no = ["no sonriendo"]
a = str(input("Como esta mono a?: "))
b = str(input("Como esta mono b?: "))
a = b

def problemas_mono_a(a_sonriendo):
    mono_a = a_sonriendo in lista_son
    if mono_a == False:
        print("Estamos en problemas")