
class Phone:

    #constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

# Instanciar o crear objectos
phone1 = Phone("Apple", "Pro12", "48mp")
phone2 = Phone("Xiomi", "Note9", "40mp")

print(phone2.marca)