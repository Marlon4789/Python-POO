
class Phone:

    #constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # Metodos
    def llamar(self):
        print(f'Estas llamando desde un: {self.modelo}')

    def cortar(self):
        print(f'Llamada finalizada desde un: {self.modelo}')

# Instanciar o crear objectos
phone1 = Phone("Apple", "Pro12", "48mp")
phone2 = Phone("Xiomi", "Note9", "40mp")

phone1.cortar()