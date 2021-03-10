#Metodos especiales Magic y Dunder
class empleado:
    aumento= 1.64
    def __init__(self,apellido,nombre,pago): #Metodo especial del constructor
        self.apellido=apellido
        self.nombre=nombre
        self.pago=pago
        self.email= nombre + '.' + apellido + '@hotmail.com'
        
    def nombre_completo(self): #Metodo de nombre completo de la clase emnpleado 
        return '{} {}'.format(self.nombre, self.apellido) #Agregando el formato de nombre y apellido concatenado

    def aplicar_aumento(self):
        self.pago=int(self.pago *  self.aumento)  #Tengo que llamar la clase empleado con la variable de la clase o atraves de self, no llamar directamente la variable

    #Metodos dunder
    def __repr__(self):
        return "empleado('{}', '{}', {})".format(self.nombre, self.apellido,self.pago)
    
    def __str__(self):
        return '{} - {}'.format(self.nombre_completo(),self.email)

    def __add__(self, otros):
        #Para sumar dos empleados y sumarle unicamente los pagos para que me de la union de ambos pagos
        return self.pago + otros.pago
    
    def __len__(self):
        return len(self.nombre_completo())

#instancias 
emp_1=  empleado('Brito', 'Franklin', 30000)
emp_2= empleado("Mora", "Laura", 20000)


#Como podemos ver en este print si no tuvieramos el metodo dunder nos daria un error al smumar los pagos pero como si lo tenemos
#lo suma sin necesidad de llamar la funcion
#print(emp_1 +emp_2)

#len para la longitud  de una lista o cadena
#print(len('test'))
#print('test'.__len__())
print(len(emp_1)) #Lo hace automatico sin llamar al metodo len que creamos


#print("--Sin llamar los metodos funciona tambien--")
#print(emp_1)
#print(repr(emp_1))
#print(str(emp_1))

#print('--Llamando los metodos especiales  repr str--')
#print(emp_1.__repr__())
#print(emp_1.__str__())


#utilizando otros metodos dunder
#print(int.__add__(1,2))
#print(str.__add__('a','b'))




#Utilizancion de los metodos dunder
#__str__: Es una representación orientada al usuario final, es la manera “informal” de representarlo
#__repr__: Es una representación “formal” de cómo se genera el objeto.
#__init__Necesito inicializar mi clase con el método __init__ para establecer los valores de la instancia.