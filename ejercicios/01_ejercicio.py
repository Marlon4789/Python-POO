class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")

nombre = input("Digame su nombre: ")
edad = input("Cual es su edad: ")
grado = input("Cual es su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    Datos del estudiante: \n 
    Nombre: {estudiante.nombre} \n 
    Edad: {estudiante.edad} \n 
    Grado: {estudiante.grado} \n 
    """)

while True:
    estudiar = input("estatus: ")
    if (estudiar.lower() == 'estudiar'):
        estudiante.estudiar()
