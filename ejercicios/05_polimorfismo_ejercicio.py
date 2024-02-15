# Crear un programa de una llave de paso de agua que cierra y abre.

class LlaveAgua:
    def abrir(self):
        pass

    def cerrar(self):
        pass

# Heredeamos de la clase LlaveAgua he implementamos los metodos.
class LlaveAguaDePaso(LlaveAgua):
    def abrir(self):
        print("La llave de paso esta abierta.")

    def cerrar(self):
        print("La llave de paso esta cerrada.")

class TanqueAgua:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.nivel_agua = 0
    
    def llenar(self, cantidad_agua):
        self.nivel_agua += cantidad_agua
        print(f"El tanque de agua se ha llenado. Nivel actual: {self.nivel_agua}")

    def esta_lleno(self):
        return self.nivel_agua >= self.capacidad_maxima
    
def main():
    tanque = TanqueAgua(capacidad_maxima=100)
    llave = LlaveAguaDePaso()

    while True:
        if tanque.esta_lleno():
            llave.cerrar()
        else:
            llave.abrir()
            tanque.llenar(10)

        input("Precionar enter para continuar...")

if __name__ == "__main__":
    main()