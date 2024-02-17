# Decorador property o propiedad => Son un tipo de propiedad que son getters, setters y deleters.

# Esto nos permite usar los metodos como si fueran propiedades.

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    # Decorador para acceder como una propiedad
    @property
    def nombre(self):
        return self.__nombre
    
    # Decorador para modificar una propiedad.
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    # Eliminar valores y metodos.
    @nombre.deleter 
    def nombre(self):
        del self.__nombre

toby = Persona("Lucas")

nombre = toby.nombre # aqui es donde se usa el metodo como una propiedad. Se quita los parentesis.
print(nombre)

# Cambiar nombre
toby.nombre = "Riki"

nombre = toby.nombre
print(nombre)

del toby.nombre

