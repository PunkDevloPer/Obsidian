# herencia multiple en python

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = False

    def acelerar(self):
        self.acelera = False

    def frenar(self):
        self.frena = False

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Furgoneta (Vehiculo):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(Vehiculo):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

    pass


MiMoto = Moto("Honda", "CBR")
MiMoto.caballito()
MiMoto.estado()
MiMoto.arrancar()
print("\n")
Mifurgoneta = Furgoneta("Renault", "Kangoo")
Mifurgoneta.arrancar()
Mifurgoneta.estado()
print(Mifurgoneta.carga(False))
