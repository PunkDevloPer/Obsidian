"""Objeto coche y sus propiedades"""


class Coche():
    """Objeto coche y sus propiedades"""
    largochasis = 200
    anchochasis = 120
    ruedascoche = 4
    enmarcha = False

    def start(self):
        """cambia el estado del coche"""
        self.enmarcha = True

    def estate(self):
        """Comprueba si el coche esta en marcha"""
        if self.enmarcha:
            print("El coche esta en marcha")
        else:
            print("El coche esta parado")


# instanciar una clase a un objeto
micoche = Coche()
print("el largo del coche es: ", micoche.largochasis)
print("el coche tiene ", micoche.ruedascoche, "ruedas")
micoche.start()
micoche.estate()
