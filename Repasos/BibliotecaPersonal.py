class Libro:
    def __init__(self, titulo, autor, codigo_isbn, disponible, veces_prestado):
        self.titulo = titulo
        self.autor = autor
        self.codigo_isbn = codigo_isbn
        self.__disponible = True
        self.__veces_prestado = 0
        