class Colaborador:
    """Representa al colaborador y se almacena la informacion basica del mismo.

    Atributos:
        nombre: nombre del colaborador.
        institucion: institucion a la cual pertenece el colaborador.
        area: area de especialidad del colaborador.
    """
    
    def __init__(self, nombre, institucion, area):
        self.nombre = nombre
        self.institucion = institucion
        self.area = area
    

    def get_informacion(self):
        return f"Nombre: {self.nombre} Institucion: {self.institucion} Area: {self.area}"
    """Metodo que muestra la informacion basica del colaborador.

    """
class Rol:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion

    def get_informacion(self):
        return f"Titulo del puesto asignado: {self.titulo}, Descripcion: {self.descripcion}"
    """Metodo que muestra la informacion del rol de cada colaborador.
    
    """
class Proyecto:
    def __init__(self, nombre_proye, descripcion):
        self.nombre_proye = nombre_proye
        self.descripcion = descripcion
        self.colaboradores = []

    def agregar_colaborador(self, colaborador: Colaborador, rol: Rol):
        self.colaboradores.append((colaborador, rol))
    """Metodo que agrega al colaborador a una lizta.
        
    """

    def mostrar_proyecto(self):
        """Se mostrarán todos los datos del proyecto.
        """
        print(f"Proyecto: {self.nombre_proye}")
        print(f"Objetivo: {self.descripcion}")
        print("Colaboradores:")
        for colab, rol in self.colaboradores:
            print(f"{colab.nombre}, Institucion: {colab.institucion}  Rol: {rol.titulo}")
        


def main():
    proyecto = Proyecto("Campaña de marketing", "Obtener mayor publico")
    rol1 = Rol("Lider del proyecto", "Encargada de organizar el trabajo")
    colab1 = Colaborador("Kimberly", "UABC", "CEO")
    proyecto.agregar_colaborador(colab1, rol1)
    proyecto.mostrar_proyecto()

    proyecto2 = Proyecto("Comida", "servir la comida para un evento.")
    rol2 = Rol("Chef", "Encargador de cocinar")
    colab2 = Colaborador("Ismael Haaz", "UTT", "Lic. RRHH")
    proyecto2.agregar_colaborador(colab2, rol2)
    proyecto2.mostrar_proyecto()

    help(Colaborador)
    help(Rol)
    help(Proyecto)
main()