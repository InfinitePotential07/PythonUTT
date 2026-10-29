class PantallaProyector:
    def __init__(self, resolucion, marca):
        self.resolucion = resolucion
        self.marca = marca

    def __str__(self):
        return f"Resolución {self.resolucion}ppx \nMarca: {self.marca}"

class Pelicula:
    def __init__(self, titulo, duracion):
        self.___titulo = titulo
        self.___duracion = duracion

    @property
    def titulo(self):
        return self.___titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.___titulo = nuevo_titulo

    @property
    def duracion(self):
        return self.___duracion
    
    @duracion.setter
    def duracion(self, nueva_duracion):
        self.___duracion = nueva_duracion

    def get_info(self):
        return f"Título: {self.__titulo}\nDuración: {self.__duracion}min."

class Empleado:
    def __init__(self, id_empleado, nombre):
        self.nombre = nombre
        self.id_empleado = id_empleado
    def __str__(self):
        return f"ID: {self.id_empleado}\nNombre: {self.nombre}"

class Sala:
    def __init__(self, numero_sala, asientos_totales):
        self.numero_sala = numero_sala
        self.asientos_totales = asientos_totales
        self.__cartelera = []
        self.__pantalla = None

    def agregar_pantalla(self, pantalla):
        if isinstance(pantalla, PantallaProyector):
            if pantalla != self.__pantalla:
                self.__pantalla = pantalla
            else:
                print("Esta pantalla está en uso.")
        else:
            print("Error")

    def agregar_a_carterela(self, pelicula):
        if isinstance(pelicula, Pelicula):
            self.__cartelera.append(pelicula)
        else:
            print("Error")

    def mostrar_cartelera(self):
        print("Cartelera sala No.{self.numero_sala} Numero de asientos: {self.asientos_totales}")
        for pelicula in self.__cartelera:
            print(pelicula.get_info())

    def __str__(self):
        return f"Sala No.: {self.numero_sala} Numero de asientos: {self.asientos_totales}"

class Cine:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.__salas = []
        self.__empleados = []

    def crear_sala(self, numero, asientos, nueva_pantalla):
        nueva_sala=Sala(numero, asientos)
        nueva_sala.agregar_pantalla(nueva_pantalla)
        self.__salas.append(Sala(numero, asientos))

    def agregar_pelicula(self, pelicula):
        sala = int(input("Ingresa el numero de sala"))
        for s in self.__salas:
            if s.numero_sala == sala:
                s.agregar_cartelera(pelicula)


    def mostrar_info(self):
        print(f"Cine {self.nombre}\nUbicacion: {self.direccion}")
        print("Salas disponibles")
        for s in self.__salas:
            print(s)
            s.mostrar_cartelera()

def main():
    cine1 = Cine("Cinepolis", "Calle 1 num. 54")
    pelicula1 = Pelicula("X-men", 70)
    pelicula2 = Pelicula("Las cronicas de Narnia: El sobrino del mago", 130)
    cine1.crear_sala(1,40, pantalla1)
    cine1.crear_sala(2, 45, pantalla1)
    pantalla1 = PantallaProyector(345, "Canon")
    cine1.agregar_pelicula(pelicula1)
    cine1.agregar_pelicula(pelicula2)
    cine1.mostrar_info()
main()
