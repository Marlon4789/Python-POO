class Elemento:
    def __init__(self, fuego):
        self.fuego = fuego

    def mostrar(self):
        return 'Soy elemento fuego'

class Nave:
    def __init__(self, barco):
        self.barco = barco

    def transporte(self):
        return 'Viaje por el mar'

# Herencia multiple
class ElementoNave(Elemento, Nave):
    def __init__(self, fuego, barco, combustion, pasageros):
        Elemento.__init__(self, fuego)
        Nave.__init__(self, barco)
        self.combustion = combustion
        self.pasageros = pasageros

    def detalles(self):
        print (f"{self.transporte()} por que {super().mostrar()} y me voy en {self.combustion} y van conmigo {self.pasageros}")

usuario = ElementoNave('Fuego', 'Lancha', 'Gas', 45)

usuario.detalles()