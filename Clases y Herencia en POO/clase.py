#Command+k Limpiar pantalla
#Un construtor es un metodo especial que le da estado inicial a los objetos._
class Coche():
    def __init__(self): #constructor
        self.__largoChasis= 250
        self.__anchoChasis=120
        self.__ruedas=4 #Los dos guiones bajos significa encapsulando ruedas para que no sea modificada fuera de la clase
        self.__enmarcha=False

    def arrancar (self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"

        else:
            return "El Coche esta parado"

    def estado(self):
        print("El coche tiene", self.__ruedas ,"ruedas. Un ancho de ", self.__anchoChasis, "y un largo de", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando un chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche= Coche()  #Intanciando clase


#Accediendo a las propiedades
#print("EL largo del chasis es: ", miCoche.largoChasis)
#print("EL coche tiene : ", miCoche.ruedas, "ruedas")

#accediendo a los metodos

#arracando el coche
print(miCoche.arrancar(True))
#estado del coche
miCoche.estado()

#Creando el segundo objeto
print("---------Creando el segundo objeto----------")

#creando mi segunda instancia
miCoche2=Coche()

#print("EL largo del chasis es: ", miCoche2.largoChasis)
#print("EL coche tiene : ", miCoche2.ruedas, "ruedas")
#arracando el coche
print(miCoche2.arrancar(False))
miCoche2.__ruedas=2
miCoche2.estado() #Estado del coche