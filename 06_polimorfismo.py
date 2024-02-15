# Polimorfismo

class Gato():
    def sonido(self):
        return "Miaw"
    
class Perro():
    def sonido(self):
        return "Guaw"
    
def hacer_sonido(animal):
    # polimorfismo 2
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

# Tipo de polimorfismo 1
print(gato.sonido())

# Tipo de polimorfismo 2
hacer_sonido(gato)

# Ejemplo 2

def recorrer(elemento):
    for item in elemento:
        print(f"El elemento es: {item}")

lista = [1,2,3,4]
lista2 = ["maquina", "carro", "volcan"]

recorrer(lista)
