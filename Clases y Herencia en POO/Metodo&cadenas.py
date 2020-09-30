#Usando metodos para manipular cadenas.
#Setring
#Metodo upper() convierte a mayuscula todas las letras de un string
#El metodo lower() convierte a miniscula todas las letras de un string
#Capitalize() convierte la primera letra en mayuscula
#Conunt() contar cuantas veces aparece una letra o una cadena de carateres
#find() representa el indice o la posicion donde aparece una letra
#isdigit() dice si el valor es un valor numerico o no (True o false)
#isalum() comprobar si es alfa numericos
#Isalpha( ) si hay solo letras y los espacios no cuentan
#split() separa por palabras utilizando espacios
#strip() borra espacios sobrantes al principio y al final
#replace() Cambia una palabra o letra por otra
#rfind() representar el indice de un caracter contando de atras 

#nombreUsuario=input("Introduce tu nombre de Usuario: ")

#print(f"El nombre de usuario es: {nombreUsuario.capitalize()}")


#Llamando al archivo de herencia donde esta la clase de vehiculos

from herencia import *

miCoche= Vehiculos("Honda","98")
miCoche.estado()