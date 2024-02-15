# Encapsulamiento => Para hacer que una clase sea privada o muy privada se usa '_' y muy privada doble guión bajo '__'.

class MiClase:
    def __init__(self) -> None:
        self.__atributo_privado = "Valor"

    # Metodos
    def __hablar(self):
        print("Soy un metodo")

mi_clase = MiClase()
print(mi_clase.__hablar())