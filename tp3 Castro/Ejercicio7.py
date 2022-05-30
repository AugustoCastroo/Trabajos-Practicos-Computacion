#Ejercicio 7. Escribir un programa, que dado un archivo de texto, un delimitador, 
#y una lista de campos, imprima solamente esos campos, separados por ese delimitador.

class read_txt_file:
    def __init__(self, text, separator):
        self.text = text
        self.separator = separator
    
    def read_text(self):
        self.separator = input("Ingrese el delimitador: ")
        file = open(self.text, "r")
        read_lines = file.readlines()
        new_string = ' '.join(read_lines)
        my_list = new_string.split(" ")
        new_string1 = self.separator.join(my_list)
        print(new_string1)

text_example = read_txt_file(r"C:\Computacion\tp3 Castro Augusto\Ej7.txt", " ")
print(text_example.read_text())

