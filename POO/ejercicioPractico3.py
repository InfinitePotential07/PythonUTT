class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' se agregó a la biblioteca con exito.")

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"El libro '{libro.titulo}' se eliminó de la biblioteca con exito.")
        else:
            print("Este libro no se encuentra en la biblioteca.")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("\nLibros disponibles en la biblioteca:")
            for libro in self.libros:
                print(f"Título: {libro.titulo}")
                print(f"Autor: {libro.autor.nombre}")
                print(f"Nacionalidad: {libro.autor.nacionalidad}")

def main():    
    autor1 = Autor("Stephen King", "Estadounidense")
    autor2 = Autor("J.K. Rowling", "Britanica")
    libro1 = Libro("La niebla", autor1)
    libro2 = Libro("Harry Potter y el prisionero de Azkaban", autor2)

    biblioteca = Biblioteca()

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.mostrar_libros()
    biblioteca.eliminar_libro(libro1)
    biblioteca.mostrar_libros()
main()
