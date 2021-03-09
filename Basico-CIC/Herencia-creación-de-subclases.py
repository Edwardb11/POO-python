#Herencia

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

#Creando clase Developer que heredara de empleado
class developer(empleado):
    #camiabdo el aumento a un 10%
    aumento=1.10
    #Para añadir un nuevo atributo a inicializar para no reescribir todo ese codigo usamos el metodo super()
    def __init__(self,apellido,nombre,pago,Leng_programacion): 
        super().__init__(apellido,nombre,pago) #Estos son los paramtros que hereda mas el que añadire abajo que es el que agregare
        self.Leng_programacion=Leng_programacion


#Creando clase manager que heredara de empleado tambien
class Manager(empleado):
        def __init__(self,apellido,nombre,pago,Empleados=None): #valor predeterminado en none para controlarlo debajo
            super(). __init__(apellido,nombre,pago)
            if Empleados is None:
                self.Empleados=[]
            else:
                self.Empleados = Empleados
            
        def agregar_Emp(self, empl):
            if empl not in self.Empleados:
                self.Empleados.append(empl)
                
        def eliminar_Emp(self, empl):
            if empl  in self.Empleados:
                self.Empleados.remove(empl)
        
        def print_empl(self):
            for empl in self.Empleados:
                print('-->', empl.nombre_completo())
                

#INSTANCIA DE CLASES
dev_1=  developer('Franklin', 'Brito', 30000, "Python")
dev_2= developer("Laura", "Mora", 20000, "Java")


#para saber si es intancia de que clase
print(isinstance(dev_1,developer))

#Para saber si es subclase de que clase
print(issubclass(developer, empleado))




#man_1=Manager('Edward', 'Brito', 90000,[dev_1])
#print(man_1.email)

#Instancia de manager
man_1=Manager('Edward', 'Brito', 90000,[dev_1])
#print(man_1)

#Agregando empleado
man_1.agregar_Emp(dev_2)

#Eliminando empleado
man_1.eliminar_Emp(dev_1)
man_1.print_empl()
#print(help(developer))
#print(dev_1.Leng_programacion)
#dev_1.aplicar_aumento()
#print(dev_1.pago)
