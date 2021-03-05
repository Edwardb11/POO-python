#python Orientado a objetos
class empleado:
    def __init__(self,apellido,nombre,pago): #Metodo especial del constructor
        self.apellido=apellido
        self.nombre=nombre
        self.pago=pago
        self.email= nombre + '.' + apellido + '@hotmail.com'
        
    def nombre_completo(self): #Metodo de nombre completo de la clase emnpleado 
        return '{} {}'.format(self.nombre, self.apellido) #Agregando el formato de nombre y apellido concatenado


#INSTANCIA DE CLASES
empleado1=  empleado('Franklin', 'Brito', 30000)
empleado2= empleado("Laura", "Mora", 20000)

#accediendo a las propiedades
print(empleado1.email)
print(empleado1.nombre_completo())

#Estas dos lineas hacen lo mismo
empleado1.nombre_completo()
empleado.nombre_completo(empleado1)


#No es necesario hacerlo asi porque utilizamos el construtor para inicializar las propiedades para luego pasarle datos

#pripiedades propia de cada instancia
#empleado1.apellido='Brito'
#empleado1.nombre= 'Edward'
#empleado1.email='edward.brito11@hotmail.com'
#empleado1.pago='50000'

#pripiedades propia de cada instancia
#empleado2.apellido='Brito'
#empleado2.nombre= 'Francina'
#empleado2.email='Francina.brito@hotmail.com'
#empleado2.pago='60000'



#print(empleado2)
#print(empleado1)