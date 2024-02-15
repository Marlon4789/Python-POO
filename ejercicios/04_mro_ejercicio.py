class Animal:
    def comer(self):
        print('El animal come')

class Mamifero(Animal):
    def amamantar(self):
        print('El mamifero amamanta')

class Ave(Animal):
    def volar(self):
        print('El ave vuela')

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

#print(Murcielago.mro())
