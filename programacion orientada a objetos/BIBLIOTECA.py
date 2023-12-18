import json

class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.año_publicacion}) - Disponible: {self.disponible} - Unidades: {self.unidades}"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_disponibles = []

    def mostrar_libros(self):
        print(f"Libros disponibles en la biblioteca '{self.nombre}':")
        for libro in self.libros_disponibles:
            print(libro)
        print("----------------------")

    def prestar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.disponible and libro.unidades > 0:
                libro.disponible = False
                libro.unidades -= 1
                print(f"Se prestó el libro '{titulo}' de la biblioteca '{self.nombre}'.")
                return
        print(f"El libro '{titulo}' no está disponible en la biblioteca '{self.nombre}'.")

    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                libro.unidades += 1
                print(f"Se recibió el libro '{titulo}' en la biblioteca '{self.nombre}'.")
                return
        print(f"El libro '{titulo}' no puede ser recibido en la biblioteca '{self.nombre}'.")

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Se agregó el libro '{libro.titulo}' a la biblioteca '{self.nombre}'.")

    def quitar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                self.libros_disponibles.remove(libro)
                print(f"Se quitó el libro '{titulo}' de la biblioteca '{self.nombre}'.")
                return
        print(f"El libro '{titulo}' no está en la biblioteca '{self.nombre}'.")

    def guardar_en_json(self):
        data = {
            "nombre": self.nombre,
            "libros": [
                {"titulo": libro.titulo, "autor": libro.autor, "año_publicacion": libro.año_publicacion, "disponible": libro.disponible, "unidades": libro.unidades}
                for libro in self.libros_disponibles
            ]
        }
        with open(f"{self.nombre}_libros.json", "w") as file:
            json.dump(data, file)
        print(f"Datos de la biblioteca '{self.nombre}' guardados en JSON.")

    def cargar_desde_json(self, archivo_json):
        try:
            with open(archivo_json, "r") as file:
                data = json.load(file)
                self.nombre = data["nombre"]
                self.libros_disponibles = [Libro(libro["titulo"], libro["autor"], libro["año_publicacion"], libro["unidades"])
                                           for libro in data["libros"]]
            print(f"Datos de la biblioteca '{self.nombre}' cargados desde JSON.")
        except FileNotFoundError:
            print(f"No se encontró el archivo JSON '{archivo_json}'.")

# Ejemplo de uso:
biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca2 = Biblioteca("Biblioteca Municipal")

# Agregar libros a las bibliotecas
libro1 = Libro("Harry Potter", "J.K. Rowling", 1997, 5)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 3)
libro3 = Libro("1984", "George Orwell", 1949, 2)

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)

biblioteca2.agregar_libro(libro2)
biblioteca2.agregar_libro(libro3)

# Mostrar libros disponibles
biblioteca1.mostrar_libros()
biblioteca2.mostrar_libros()

# Prestar y recibir libros
biblioteca1.prestar_libro("Harry Potter")
biblioteca1.mostrar_libros()

biblioteca2.recibir_libro("Harry Potter")
biblioteca2.mostrar_libros()

# Guardar y cargar desde JSON
biblioteca1.guardar_en_json()
biblioteca1 = Biblioteca("Biblioteca Central")  # Simulando una nueva instancia de la biblioteca
biblioteca1.cargar_desde_json("Biblioteca Central_libros.json")
biblioteca1.mostrar_libros()
