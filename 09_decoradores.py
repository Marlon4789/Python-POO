# Es la manera de agregar un código extra antes o despues de una ejecución de una function.

def decorador(funcion):
    def funcion_modificada():
        funcion()
        print("Antes de llamar a la funcion")
        
    return funcion_modificada

@decorador
def saludo():
    print("Hola toby")

saludo()

# Esta es la manera normal
# def saludo():
#     print("Hola Toby")

# saludo_modificado = decorador(saludo)
# saludo_modificado()
