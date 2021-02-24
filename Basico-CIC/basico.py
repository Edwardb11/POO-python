#Una clase es solo una colección organizada de variables y funciones. Las clases se definen de forma similar a las funciones, con la siguiente sintaxis:
class MyClass(object):
    
    i = 123

    def say_hello(self):
        return 'Hi there!'
    
#Para utilizar una clase, puede crear una representación de esa clase, denominada instancia u objeto , 
# y asignarla a una variable. Por ejemplo:
a = MyClass()

#Luego puede llamar a las funciones y variables definidas dentro de la clase:
print (a.i)
#123
print (a.say_hello())
#'Hi there!'

#La sintaxis que usamos para definir una clase puede variar según las preferencias. Por ejemplo, podríamos 
# haber definido MyClass:
class MyClass(object):
    
    def prepare(self):
        self.i = 123

    def say_hello(self):
        return 'Hi there!'
    
#La selfvariable representa el objeto en sí, y la usamos dentro de los procedimientos para
#referirnos a otras funciones y variables que están definidas dentro del alcance de nuestra clase. 
#Cuando hablamos del alcance de una variable, estamos hablando de la región en un programa en el que 
#podemos acceder a esa variable. Por ejemplo, supongamos que tenemos el programa básico:    
x = 2
y = 3
def add_nums():
    x = 5
    y = 6
    return x + y

print (add_nums())



#Instanciación
#La operación de instanciación ("llamar" a un objeto de clase) crea un objeto vacío. A muchas clases
#les gusta crear objetos con instancias personalizadas para un estado inicial específico. Imitamos 
#este comportamiento con nuestra preparefunción, pero Python tiene un método incorporado especial llamado __init__(),
#que evalúa cuando se crea el objeto, para manejar este tipo de inicialización de objeto:

class MyClass(object):
    def __init__(self):
        self.i = 123

a = MyClass()

print (a.i)
#123


#Herencia

#Ahora, digamos que queremos crear dos clases que sean muy similares en funcionalidad, pero no completamente idénticas. 
# Por ejemplo, queremos una clase que pueda 'saludar' y que almacene un número entero en la variable 'i', pero queremos 
# otra clase que pueda hacer todas esas mismas cosas, además de 'saludar'. Para lograr esto, podemos usar la idea de 
# herencia en la programación orientada a objetos. La herencia describe el proceso de configurar varias clases donde 
# una o más de estas clases hereda la funcionalidad de otra clase base. Para escribir nuestro ejemplo en código:

class MyClass(object):

    def __init__(self):
        self.i = 123

    def say_hi(self):
        return 'Hi there!'

class MyBetterClass(MyClass):

    def say_hello(self):
        return 'Hello!'

a = MyBetterClass()
print (a.say_hello())
#Hello!

print (a.say_hi())
#Hi there!

print (a.i)
#123