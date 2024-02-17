# La abstracción es la forma de ocultar la complejidad de un sistema. 

# Ejemplo: ocultar la complejidad de un login internamente y solo mostrar lo importante del login, como el formulario y los botones.

class Auto:
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encender"
        print("El auto esta encendido")

    def conducir(self):
        if self._estado == "encender":
            self.encender()
            print("Conduciendo el auto")
        else:
            print("El auto esta apagado")

mi_auto = Auto()
mi_auto.conducir()