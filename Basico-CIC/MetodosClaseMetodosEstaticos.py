#Metodos estaticos y metodos de clases
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

    @classmethod  #Basicamente este metodo esta alterando la funcionalidad de nuestro metodo a donde ahora 
    #recibimos una clase como primer argumento en lugar de la instancia ahora por convencion con un metodo 
    #regular que llamemos esta instancia
    def establecer_Monto_Aum(cls,monto):
        cls.aumento=monto
    
    @classmethod
    def from_string(cls,emp_str):
        apellido,nombre,pago = emp_str.split('-') #trabajando con esta cadenda especificamente, voy a divir
        #la cadena que pasan a este metodo, asi en lugar de la cadena a cada un de los empleado uso esto
        return cls(apellido,nombre,pago) #Aqui se crea ese nuevo empleado y retornar ese objeto empleado cuando se llama este metodo
    
    
    @staticmethod  #se utiliza cuando no accedes a ninguna instancia a al class
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6: #5 Sabado 6 Domingo  
            return False
        return True
  
#INSTANCIA DE CLASES
empleado1=  empleado('Franklin', 'Brito', 30000)
empleado2= empleado("Laura", "Mora", 20000)

print('--Verificando el aumento que obtendra cada empleado--')
empleado.establecer_Monto_Aum(1.05)  #Establesco un monto a todo con el metodo creado arriba
print(empleado1.aumento)
print(empleado.aumento)
print(empleado2.aumento)

#Si un empleado se crea a partir de una cadena podemos usar el metodo .split apartir de aqui:
emp_str_1= 'Brito-Edward-2000'
emp_str_2='Lane-Jordan-3000'
emp_str_3='Salsedo-Joan-4000'

new_emp_1=empleado.from_string(emp_str_1)

#apellido,nombre,pago=emp_str_1.split('-') #En esta linea de codigo esta la magia ya son los elementos que tiene nuestra clase
#new_emp_1=empleado(apellido,nombre,pago) #Aqui esta la instancia de la clase atravez de string usando .split

print(new_emp_1.email)
print(new_emp_1.pago)

#Fecha y que devuelva si el dia fue laborable o por lo que hare un metodo estatico arriba

import datetime

#El datetimemódulo proporciona clases para manipular fechas y horas.
#con .date puede acceder año, mes, dia
my_date=datetime.date(2016,7,19) 
print(empleado.is_workday(my_date))


#En conclusion la diferencia entre los metodos de instancias regulares metodos de clases que pueden
#tambien se pueden utilizar como constructores alternativos y que los metodos estaticos que no funcionan
#en las instancias o en la clase 