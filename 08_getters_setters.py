# Getters y Setters => es la manera en la que accedemos a los metodos privados y poderlos modificar.

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self._edad = edad

    # Obtener
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

persona = Persona("toby", 56)

nombre = persona.get_nombre()
print(nombre)

persona.set_nombre("Escanor")

nombre = persona.get_nombre()
print(nombre)

