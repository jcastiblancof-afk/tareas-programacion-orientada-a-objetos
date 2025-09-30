# -----------------------------------
# Simulador de Biblioteca Universitaria
# Programación Orientada a Objetos
# -----------------------------------

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria):
        self.__titulo = titulo         # Atributo privado (encapsulado)
        self.__autor = autor
        self.__categoria = categoria
        self.__disponible = True       # Por defecto un libro nuevo está disponible

    # Métodos Getters
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_categoria(self):
        return self.__categoria
    
    def esta_disponible(self):
        return self.__disponible

    # Método para cambiar disponibilidad (ej: préstamo)
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False
    
    def devolver(self):
        self.__disponible = True

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"{self.__titulo} - {self.__autor} [{self.__categoria}] - {estado}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__prestamos = []   # lista de libros prestados

    def get_nombre(self):
        return self.__nombre
    
    def get_codigo(self):
        return self.__codigo

    def prestar_libro(self, libro: Libro):
        if libro.prestar():
            self.__prestamos.append(libro)
            print(f"{self.__nombre} ha prestado el libro: {libro.get_titulo()}")
        else:
            print(f"El libro {libro.get_titulo()} no está disponible.")

    def devolver_libro(self, libro: Libro):
        if libro in self.__prestamos:
            libro.devolver()
            self.__prestamos.remove(libro)
            print(f"{self.__nombre} devolvió el libro: {libro.get_titulo()}")
        else:
            print(f"{self.__nombre} no tiene prestado el libro {libro.get_titulo()}")

    def __str__(self):
        return f"Usuario: {self.__nombre} (Código: {self.__codigo})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []
        self.__usuarios = []

    # Registro de libros
    def registrar_libro(self, titulo, autor, categoria):
        libro = Libro(titulo, autor, categoria)
        self.__libros.append(libro)

    # Registro de usuarios
    def registrar_usuario(self, nombre, codigo):
        usuario = Usuario(nombre, codigo)
        self.__usuarios.append(usuario)

    # Buscar libro
    def buscar_libro(self, titulo):
        for libro in self.__libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None

    # Buscar usuario
    def buscar_usuario(self, codigo):
        for usuario in self.__usuarios:
            if usuario.get_codigo() == codigo:
                return usuario
        return None

    # Mostrar catálogo de libros
    def mostrar_libros(self):
        print("\n--- Catálogo de Libros ---")
        for libro in self.__libros:
            print(libro)

    # Mostrar usuarios registrados
    def mostrar_usuarios(self):
        print("\n--- Lista de Usuarios ---")
        for usuario in self.__usuarios:
            print(usuario)


# ------------------------------
# Ejemplo de uso del sistema
# ------------------------------
if __name__ == "__main__":
    biblioteca = Biblioteca("Biblioteca UNAL")

    # Registro de libros (mínimo 3 categorías)
    biblioteca.registrar_libro("Cien años de soledad", "Gabriel García Márquez", "Novela")
    biblioteca.registrar_libro("Introducción a la programación", "John Smith", "Académico")
    biblioteca.registrar_libro("Breve historia del tiempo", "Stephen Hawking", "Ciencia")

    # Registro de usuarios
    biblioteca.registrar_usuario("Juan Pérez", "U001")
    biblioteca.registrar_usuario("María López", "U002")

    # Mostrar datos
    biblioteca.mostrar_libros()
    biblioteca.mostrar_usuarios()

    # Préstamo de libro
    usuario = biblioteca.buscar_usuario("U001")
    libro = biblioteca.buscar_libro("Cien años de soledad")
    if usuario and libro:
        usuario.prestar_libro(libro)

    # Intentar prestar el mismo libro (ya prestado)
    otro_usuario = biblioteca.buscar_usuario("U002")
    if otro_usuario and libro:
        otro_usuario.prestar_libro(libro)

    # Devolver libro
    usuario.devolver_libro(libro)

    # Catálogo actualizado
    biblioteca.mostrar_libros()
