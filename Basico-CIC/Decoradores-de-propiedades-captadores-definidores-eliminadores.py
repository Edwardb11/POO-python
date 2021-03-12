class empleado:
    def __init__(self,apellido,nombre):
        self.apellido=apellido
        self.nombre=nombre
        
    @property    
    def email(self): 
        return '{}.{}@hotmail.com'.format(self.nombre, self.apellido) 
    
    @property
    def nombre_completo(self): #Metodo de nombre completo de la clase emnpleado 
        return '{} {}'.format(self.nombre, self.apellido) #Agregando el formato de nombre y apellido concatenado
    
    @nombre_completo.setter #Definiendo 
    def nombre_completo(self,nombre):
        nombre,apellido=nombre.split(' ') #split convierte una cadena de texto en una lista. 
        self.nombre=nombre
        self.apellido=apellido
        
    @nombre_completo.deleter #Eliminando 
    def nombre_completo(self):
        print("Borrando nombre completo")
        self.nombre=None
        self.apellido=None
    
emp_1=empleado('Brito', 'Edward')
emp_1.nombre_completo= 'Edward Brito'

emp_1.nombre='Jim' #Aqui estoy cambiando el atributo nombre 
print(emp_1.nombre)
print(emp_1.email)
print(emp_1.nombre_completo)


del emp_1.nombre_completo

#el trabajo principal de los decoradores es que se utilizan para agregar 
# funcionalidad al código existente. También llamado metaprogramación,
# como parte del programa, intenta modificar otra parte del programa en 
# tiempo de compilación.
