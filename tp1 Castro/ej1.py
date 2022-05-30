lista_sem = ["lunes", "martes", "miércoles", "jueves", "viernes"]
lista_dormir = ["sabado", "domingo", "enero", "febrero"]
dia = str(input("¿?Que dia de la semana es?: "))

def dia(dia_semana):
    a = dia_semana in lista_dormir
    if a == False:
        print("a laburar")
    else:
        print("a mimir")

def mes(vaca):
    b = vaca in lista_dormir
    if b == True:
        print("a mimir")
print("¿En que mes estamos?: ")
vacaciones = str(input())
vaca = vacaciones
mes(vaca)
final = vaca in lista_dormir
if final == False:
    print("¿Que dia de la semana es?: ")
    dia_semana = str(input())
    dia_semana = dia_semana.lower()
    dia(dia_semana)