#Por ejemplo, quizás nuestro objeto Maryo pueda 'hablar', tenga coordenadas de posición y un estado de estar 'vivo' o 'muerto':

class Maryo(object):
    #position coordinates
    x = 50
    y = 0

    #properties
    alive = True

    #actions
    def say_hi(self):
        if self.alive:
            print ("It's me! Maryo!")
        else:
            print ("This Maryo disappeared")

    def poof(self):
        self.alive = False
        
#Nuestro objeto Árbol puede 'crecer', tiene coordenadas de posición y un estado de estar 'vivo' o 'muerto':

class Tree(object):
    #position coordinates
    x = 60
    y = 0

    #properties
    alive = True

    size = 3

    #actions
    def grow(self):
        if self.alive:
            self.size += 1
            print ('Grew to be %s meters tall' % self.size)
        else:
            print ('This tree disappeared')

    def poof(self):
        self.alive = False
#Y nuestro objeto monstruo puede 'comer', tiene coordenadas de posición y un estado de estar 'vivo' o 'muerto'.

class Monster(object):
    #position coordinates
    x = 85
    y = 10

    #properties
    alive = True

    size = 5

    #actions
    def eat(self):
        if self.alive:
            self.size += 5
            print ('Yum!')
        else:
            print ('This monster disappeared')

    def poof(self):
        self.alive = False
#¡Lindo! Entonces ahora tenemos un modelo programático básico de nuestro mundo. Pero , tenemos que notar que muchos de 
# nuestros objetos comparten propiedades y atributos similares, como coordenadas de posición, estado y la desafortunada
# habilidad de 'poof'. Quizás nuestro modelo se beneficiaría de la simplicidad si nuestros objetos heredaran estas propiedades 
# y atributos de un charactermodelo base :

class Character(object):

    def __init__(self, x, y, size = None):
        self.x = x
        self.y = y
        self.size = size
        self.alive = True

    def poof(self):
        self.alive = False
        print ('Poof!')

class Maryo(Character):

    def say_hi(self):
        if self.alive:
            print ("It's me! Maryo!")
        else:
            print ("This Maryo disappeared")

class Tree(Character):

    def grow(self):
        if self.alive:
            self.size += 1
            print ('Grew to be %s meters tall!' % self.size)
        else:
            print ('This tree disappeared')

class Monster(Character):

    def eat(self):
        if self.alive:
            self.size += 5
            print ('Yum!')
        else:
            print ('This monster disappeared')
#Entonces, para cada clase que escribimos para representar un objeto, si esa clase hereda Character, entonces solo tenemos que 
# enfocarnos en definir las propiedades y atributos específicos de ese objeto, y todas las propiedades y atributos básicos 
# se incluirán inherentemente.

#Ejemplo de cómo funciona nuestro mundo:

m, t, o = Maryo(50, 0), Tree(60, 0, 3), Monster(85, 10, 5)

print (t.size)
#3

t.grow()
#Grew to be 4 meters tall!

print (t.size)
#4

print (o.size)
#5

o.eat()
#Yum!

print (o.size)
#10

print (m.x, m.y)
#50 0

m.say_hi()
#Its me! Maryo!

m.poof()
#Poof!

m.say_hi()
#This Maryo disappeared

print (m.alive)
#False