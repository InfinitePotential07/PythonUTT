class Cancion:
    def __init__(self, titulo, duracion):
        self.__titulo = titulo
        self.__duracion = duracion
        
    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo
    def get_duracion(self):
        return self.__duracion
    def set_duracion(self, nueva_duracion):
        self.__duracion = nueva_duracion
    def __str__(self):
        return f"{self.__titulo} ({self.__duracion} seg)"
    
class Playlist:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__canciones = []
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def get_canciones(self):
        return self.__canciones
    def set_canciones(self, nueva_lista):
        if isinstance(nueva_lista, list):
            self.__canciones = nueva_lista
        else:
            print("Error: debe ser una lista")
    
    def agregar_cancion(self, cancion):
        if isinstance(cancion, Cancion):
            self.__canciones.append(cancion)
        else:
            print("Error: solo se pueden agregar canciones")
            
    def mostrar_canciones(self):
        print(self.__nombre)
        for i, cancion in enumerate(self.__canciones, start = 1):
            print(f"{i}. {cancion}")
def main():
    playlist1= Playlist("Mis Favs")
    
    cancion1 = Cancion("Dos mil 16 - Bad Bunny", 135)
    cancion2 = Cancion("RLDT - Bad Bunny", 155)
    cancion3 = Cancion("Tommy Lee - Post Malone", 157)
    
    playlist1.agregar_cancion(cancion1)
    playlist1.agregar_cancion(cancion2)
    playlist1.agregar_cancion(cancion3)
    
    playlist1.mostrar_canciones()
main()