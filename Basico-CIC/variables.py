#Variables
class empleado:
    Num_de_empleados=0
    aumento= 1.64
    def __init__(self,apellido,nombre,pago): #Metodo especial del constructor
        self.apellido=apellido
        self.nombre=nombre
        self.pago=pago
        self.email= nombre + '.' + apellido + '@hotmail.com'
        
        empleado.Num_de_empleados+=1
    def nombre_completo(self): #Metodo de nombre completo de la clase emnpleado 
        return '{} {}'.format(self.nombre, self.apellido) #Agregando el formato de nombre y apellido concatenado

    def aplicar_aumento(self):
        self.pago=int(self.pago +  self.aumento)  #Tengo que llamar la clase empleado con la variable de la clase o atraves de self, no llamar directamente la variable

#INSTANCIA DE CLASES
empleado1=  empleado('Franklin', 'Brito', 30000)
empleado2= empleado("Laura", "Mora", 20000)


#Aumento solo al empleado 1y verificando que el aumento de los demas sea el de la vairbale de clase
empleado1.aumento=1.5
print(empleado1.__dict__) #Se puede utilizar para modificar o leer los atributos.
print('\n')
print('--Verificando el aumento que obtendra cada empleado--')
print(empleado1.aumento)
print(empleado.aumento)
print(empleado2.aumento)


#sabiendo el numero de empleado que hay
print('\n')
print('--Numeros de empleados--')
print(empleado.Num_de_empleados)


#Empleado aplicando aumento
print('\n')
print('--Empleado aplicando aumento de pago--')
print(empleado1.pago) #Sin aumento
empleado1.aplicar_aumento()
print(empleado1.pago) #con aumento porque llame el metodo

