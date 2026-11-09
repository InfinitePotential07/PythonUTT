class CPU:
    """Representa el procesador de una computadora.

    Atributos:
        modelo (str): Nombre del modelo del procesador.
        velocidad (float): Velocidad del reloj en GHz.
    """

    def __init__(self, modelo, velocidad):
        """Inicializa el procesador.

        Args:
            modelo (str): Nombre del modelo del procesador.
            velocidad (float): Velocidad del reloj en GHz.
        """
        self.modelo = modelo
        self.velocidad = velocidad

    def obtener_descripcion(self):
        """Devuelve una descripción legible del procesador.

        Returns:
            str: Texto con el modelo y la velocidad en GHz.
        """
        return f"CPU: {self.modelo}. {self.velocidad} GHz."


class RAM:
    """Representa la memoria RAM de una computadora.

    Atributos:
        capacidad (int): Capacidad total en GB.
        modelo (str): Tipo o modelo de memoria (por ejemplo, "DDR5").
    """

    def __init__(self, capacidad, modelo):
        """Inicializa la memoria RAM.

        Args:
            capacidad (int): Capacidad total en GB.
            modelo (str): Tipo o modelo de memoria.
        """
        self.capacidad = capacidad
        self.modelo = modelo

    def obtener_descripcion(self):
        """Devuelve una descripción legible de la memoria RAM.

        Returns:
            str: Texto con la capacidad en GB y el modelo.
        """
        return f"RAM: {self.capacidad} GB {self.modelo}."


class DiscoDuro:
    """Representa la unidad de almacenamiento de una computadora.

    Atributos:
        tipo (str): Tecnología de la unidad (por ejemplo, "SSD NVMe M.2").
        capacidad (int): Capacidad total en GB.
    """

    def __init__(self, tipo, capacidad):
        """Inicializa la unidad de almacenamiento.

        Args:
            tipo (str): Tecnología de la unidad.
            capacidad (int): Capacidad total en GB.
        """
        self.tipo = tipo
        self.capacidad = capacidad

    def obtener_descripcion(self):
        """Devuelve una descripción legible del almacenamiento.

        Returns:
            str: Texto con la capacidad en GB y el tipo de unidad.
        """
        return f"Almacenamiento: {self.capacidad} GB {self.tipo}"


class Computadora:
    """Representa una computadora compuesta por sus componentes de hardware.

    Atributos:
        marca (str): Fabricante del equipo.
        modelo (str): Modelo del equipo.
        CPU (CPU): Procesador instalado.
        RAM (RAM): Memoria RAM instalada.
        DiscoDuro (DiscoDuro): Unidad de almacenamiento instalada.
    """

    def __init__(self, marca, modelo, CPU, RAM, DiscoDuro):
        """Inicializa la computadora con sus componentes.

        Args:
            marca (str): Fabricante del equipo.
            modelo (str): Modelo del equipo.
            CPU (CPU): Procesador del equipo.
            RAM (RAM): Memoria RAM del equipo.
            DiscoDuro (DiscoDuro): Unidad de almacenamiento del equipo.
        """
        self.marca = marca
        self.modelo = modelo
        self.CPU = CPU
        self.RAM = RAM
        self.DiscoDuro = DiscoDuro

    def mostrar_configuracion(self):
        """Imprime en consola la configuración completa del sistema.

        Muestra la marca y el modelo, seguidos de la descripción de cada
        componente (CPU, RAM y almacenamiento).
        """
        print(f" CONFIGURACIÓN DEL SISTEMA: {self.marca} {self.modelo}")
        print(f" {self.CPU.obtener_descripcion()}")
        print(f" {self.RAM.obtener_descripcion()}")
        print(f" {self.DiscoDuro.obtener_descripcion()}")


def main():
    """Crea una computadora de ejemplo y muestra su configuración."""
    mi_cpu = CPU(modelo="Intel Core i9", velocidad=3.4)
    mi_ram = RAM(capacidad=32, modelo="DDR5")
    mi_disco = DiscoDuro(capacidad=1000, tipo="SSD NVMe M.2")
    mi_pc = Computadora(
        marca="DELL",
        modelo="CELERION",
        CPU=mi_cpu,
        RAM=mi_ram,
        DiscoDuro=mi_disco,
    )
    mi_pc.mostrar_configuracion()
main()