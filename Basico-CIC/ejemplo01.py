import  datetime
class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    datetime.date(2001, 7, 11), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())

#NOTA 
#La agefunción no toma ningún parámetro excepto selfque solo usa información
# almacenada en los atributos del objeto y la fecha actual (que recupera 
# usando el datetimemódulo).

#Nota de atributos privados
#Comenzar un atributo o nombre de método con un guión bajo ( _) es una convención que
# usamos para indicar que es una propiedad interna “privada” y no se debe acceder 
# directamente. En un ejemplo más realista, nuestro valor en caché a veces caduca y
# es necesario volver a calcularlo, por lo que siempre debemos usar el agemétodo para 
# asegurarnos de obtener el valor correcto.

#Ejemplo
# def age(self):
 ##      return self._age

   # today = datetime.date.today()

#    age = today.year - self.birthdate.year

 #   if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
  #      age -= 1

   # self._age = age
    #return age

#Debemos, sin embargo, tenga cuidado cuando un atributo de clase es de un 
# tipo mutable - porque si la modificamos en el lugar, nos vamos a afectar 
# a todos los objetos de esa clase al mismo tiempo. Recuerde que todas las 
# instancias comparten los mismos atributos de clase:

class Person:
    pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

jane = Person()
bob = Person()

jane.add_pet("cat")
print(jane.pets)
print(bob.pets) # oops!

#Lo que deberíamos hacer en casos como este es inicializar el atributo 
# mutable como un atributo de instancia , dentro __init__. Entonces, 
# cada instancia tendrá su propia copia separada:
class Person:
    
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

jane = Person()
bob = Person()

jane.add_pet("cat")
print(jane.pets)
print(bob.pets)