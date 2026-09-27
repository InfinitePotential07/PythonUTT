class Libro:
    def __init__(self, titulo, autor, codigo_isbn):
        self.titulo = titulo
        self.autor = autor
        self.codigo_isbn = codigo_isbn
        self.__disponible = True
        self.__veces_prestado = 0

    def informacion(self):
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nISBN: {self.codigo_isbn}"

    def get_veces_prestado(self):
        return self.__veces_prestado

    def set_veces_prestado(self, veces):
        self.__veces_prestado += veces

    def prestar(self):
        if self.__disponible is False:
            print(f"El libro {self.titulo}, no está disponible.")
        else:
            print("Prestamo realizado con exito!")
            self.set_veces_prestado(1)
            self.__disponible = False

    def devolver(self):
        if self.__disponible is True:
            print("El libro no está prestado.")
        else:
            print("Libro devuelto.")
            self.__disponible = True
    def estado(self):
        if self.__disponible is False:
            print(f"El libro {self.titulo} está prestado.")
        else:
            print(f"El libro {self.titulo} está disponible.")

    def esta_disponible(self):
        return self.__disponible

    def intercambiar(self, otro_libro):
        if self.__disponible is False and otro_libro.esta_disponible() is False:
            print("Intercambio exitoso")
        else:
            print("Intercambio cancelado, un libro no está prestado")

def main():
    libro1 = Libro("Juego de tronos: Cancion de hielo y fuego", "George R. R. Martin", "JDT001")
    print(libro1.informacion())
    libro1.prestar()
    print(f"El libro {libro1.titulo} ha sido prestado {libro1.get_veces_prestado()} vez/veces.")
    libro1.prestar()
    libro1.devolver()
    libro1.prestar()
    print(f"El libro {libro1.titulo} ha sido prestado {libro1.get_veces_prestado()} vez/veces.")
    libro1.estado()
    libro1.devolver()
    libro1.estado()
    print("-" * 50)
    libro2 = Libro("El exorcista", "William Platty", "EEX002")
    print(libro2.informacion())
    libro2.prestar()
    print(f"El libro {libro2.titulo} ha sido prestado {libro2.get_veces_prestado()} vez/veces.")
    libro2.prestar()
    libro2.devolver()
    libro2.prestar()
    print(f"El libro {libro2.titulo} ha sido prestado {libro2.get_veces_prestado()} vez/veces.")
    libro2.estado()
    libro2.devolver()
    libro2.estado()
    print("-" * 50)
    libro3 = Libro("It", "Stephen King", "IT003")
    libro3.prestar()          # libro3 queda prestado

    libro1.prestar()          # asumiendo que libro1 estaba disponible, ahora prestado
    libro1.intercambiar(libro3)   # ambos prestados → "Intercambio exitoso"

    libro1.intercambiar(libro2)   # libro2 disponible → "Intercambio cancelado..."

main()