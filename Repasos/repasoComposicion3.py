class Jugador:
    def __init__(self, nombre, numero):
        self.__nombre = nombre
        self.__numero = numero
        
    def __str__(self):
        return f"#{self.__numero} {self.__nombre}"
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def get_numero(self):
            return self.__numero
    def set_numero(self, nuevo_numero):
        self.__numero = nuevo_numero
        
class Equipo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__jugadores = []
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def get_jugadores(self):
        return self.__jugadores
    def set_jugadores(self, nueva_lista):
        if isinstance(nueva_lista, list):
            self.__jugadores = nueva_lista
        else:
            print("Error: debe ser una lista")
    def agregar_jugador(self, nuevo_jugador):
        if isinstance(nuevo_jugador, Jugador):
            self.__jugadores.append(nuevo_jugador)
        else:
            print("Error: debe ser un jugador")
    def mostrar_plantilla(self):
        print(f"{self.get_nombre()}")
        for i, jugador in enumerate(self.__jugadores, start = 1):
            print(f"{jugador.get_numero()} {jugador.get_nombre()}")
        
        
def main():
    equipo1 = Equipo("Xolos")
    
    jug1 = Jugador(10, "Gilberto Mora")
    jug2 = Jugador(9, "Erling Haaland")
    jug3 = Jugador(17, "Jimenez")
    
    equipo1.agregar_jugador(jug1)
    equipo1.agregar_jugador(jug2)
    equipo1.agregar_jugador(jug3)
    
    equipo1.mostrar_plantilla()
main()
        