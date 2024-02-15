
# Clase padre

class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print('Estoy trabajando')
        
# Clase hija => Herencia simple o jerarquica: que una o más clases heredan de la clase padre.
class Empleado(Persona):
    def __init__(self, nombre, edad, trabajo, salario):
        super().__init__(nombre, edad)
        self.trabajo = trabajo
        self.salario = salario

class Jefe(Persona):
    def __init__(self, nombre, edad, empresa):
        super().__init__(nombre, edad)
        self.empresa = empresa
    
    def ceo(self):
        print('Soy un buen jefe')

empleado = Empleado('Roberto', 45, 'Programador', '5.000')

jefe = Jefe('Andres', 26, 'Intel')

print(empleado.nombre)
print(jefe.empresa)

print(f'Soy el CEO {jefe.nombre} y tengo a cargo un {empleado.trabajo} al cual le pago al mes {empleado.salario} dolares, él es  {empleado.nombre}, un buen empleado')