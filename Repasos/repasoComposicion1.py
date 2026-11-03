class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__libros = []
    def agregar_libro(self, libro):
        self.__libros.append(libro)
    def mostrar_libros(self):
        print(f"{self.nombre}")
        numero = 1
        for libro in self.__libros:
            print(f"{numero}. {libro}")
            numero += 1
def main():
    #Se crea la biblioteca
    biblio1 = Biblioteca("Biblioteca Central")
    
    #Se crean los libros
    libro1 = Libro("Don Quijote", "Miguel de Cervantes")
    libro2 = Libro("Juego de tronos", "George R.R. Martin")
    libro3 = Libro("Harry Potter y el prosionero de Azkaban", "J.K. Rowling")
    
    #Se agregan los libros a la biblioteca
    biblio1.agregar_libro(libro1)
    biblio1.agregar_libro(libro2)
    biblio1.agregar_libro(libro3)
    
    #Se muestran los libros de la biblioteca
    biblio1.mostrar_libros()
main()
    