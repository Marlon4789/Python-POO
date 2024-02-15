class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad =  edad

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}, La edad es: {self.edad}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f'El grado es: {self.grado}')

estudiante = Estudiante('Sara', 25, 9)

estudiante.mostrar_datos()  
estudiante.mostrar_grado()