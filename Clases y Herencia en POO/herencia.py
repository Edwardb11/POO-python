#aprendiendo herencia en python

#Clase de vehiculos la que le heredara a los demas
class Vehiculos ():
    def __init__(self, marca, modelo):

        self.marca= marca
        self.modelo= modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar (self):
        self.enmarcha=True

    def acelerar (self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, 
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

#Clase furgoneta
class Furgoneta(Vehiculos):
     def carga(self,cargar):
         self.cargado=cargar
         if (self.cargado):
             return "La Furgoneta esta cargada"
         else:
            return "La furgoneta no esta cargada"



#Clase moto
class Moto(Vehiculos): #Esta clase hereda de la clase vehiculos

    calibrar=""
    def calibrar(self):
        self.calibrar = "Voy calibrando"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, 
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.calibrar)

#Clase de vehiculos electricos
class  Velectricos():
    def __init__(self):
        self.autonomia=100

    def cargaEnergia(self):
        self.cargando=True
    

#Clase de bisicleta electrica

class Bicicleta_Electrica(Vehiculos,Velectricos):
    pass


#Instanciando la clase moto
miMoto=Moto("Honda ", "90")
miMoto.calibrar()
miMoto.estado()

#Instanciando la clase furgoneta
miFurgoneta= Furgoneta("Honda", "Brito")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#Instanciando la bisicleta electrica
Mibisi=Bicicleta_Electrica("Mongo", "199") #se hereda primero del construtor de uno y luego del otro
Mibisi.estado()