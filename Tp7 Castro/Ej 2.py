
ask = int(input("Indique su PIN: "))
dig = len(str(ask))

def PIN(dig):
    if dig == 4:
        print("Su PIN es correcto posee", dig, "dígitos")
    elif dig == 6:
        print("Su PIN es correcto posee", dig, "dígitos")
    else:
        print("Su PIN es INCORRECTO, debe poseer 4 o 6 dígitos, NO:", dig, "dígitos")



