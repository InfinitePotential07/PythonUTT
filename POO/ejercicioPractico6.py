"""Ejercicio de composición: Docente, PlanTrabajo, Curso y RecursoDigital."""


class PlanTrabajo:
    """Representa el plan de trabajo de un docente."""

    def __init__(self, objetivos, actividades):
        """Inicializa el plan con sus objetivos y actividades."""
        self.objetivos = objetivos
        self.actividades = actividades

    def mostrar_plan(self):
        """Muestra los objetivos y actividades del plan."""
        return print(f"Objetivos: {self.objetivos} \nActividades {self.actividades}")


class Docente:
    """Representa a un docente que puede crear un plan de trabajo."""

    def __init__(self, nombre, grupo):
        """Inicializa el docente sin plan de trabajo."""
        self.nombre = nombre
        self.grupo = grupo
        self.planTrabajo = None

    def get_info(self):
        """Muestra el nombre y el grupo del docente."""
        return print(f"Nombre: {self.nombre} \nGrupo: {self.grupo}")

    def crear_plan(self, objetivos, actividades):
        """Crea el plan de trabajo del docente y lo devuelve."""
        self.planTrabajo = PlanTrabajo(objetivos, actividades)
        return self.planTrabajo


class RecursoDigital:
    """Representa un recurso digital con su tipo y su URL."""

    def __init__(self, tipo, url):
        """Inicializa el recurso con su tipo y su URL."""
        self.tipo = tipo
        self.url = url


class Curso:
    """Representa un curso con un docente y una lista de recursos."""

    def __init__(self, nombre, docente):
        """Inicializa el curso con su docente y sin recursos."""
        self.nombre = nombre
        self.docente = docente
        self.recursos = []

    def agregar_recurso(self, recurso):
        """Agrega un recurso digital a la lista del curso."""
        self.recursos.append(recurso)

    def mostrar_recurso(self):
        """Muestra todos los recursos del curso."""
        print(f"Recursos del curso {self.nombre}:")
        for recurso in self.recursos:
            print(f"{recurso.tipo}: {recurso.url}")


def main():
    """Crea un docente, su plan y un curso con un recurso, y los muestra."""
    docente1 = Docente("Karina", "A")
    docente1.get_info()
    plan1 = docente1.crear_plan(objetivos="Fundamentos matematicos", actividades="Mostrar productos notables")
    plan1.mostrar_plan()

    curso1 = Curso("Matematicas", docente1)
    video1 = RecursoDigital("Video", "youtube.com/JulioProfe/Productos-Notables")
    curso1.agregar_recurso(video1)
    curso1.mostrar_recurso()


main()