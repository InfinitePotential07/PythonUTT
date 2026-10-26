class Figura:
    """Representa una figura geométrica genérica.

    Sirve como clase base para figuras concretas, que deben
    sobrescribir el método "area".

    Atributos:
        nombre: Nombre de la figura (solo lectura).
    """

    def __init__(self, nombre):
        """Inicializa la figura con un nombre.

        Argumentos:
            nombre: Nombre de la figura.
        """
        self.__nombre = nombre

    def area(self):
        """Retorna el área de la figura, que en la clase base es 0."""
        return 0

    @property
    def nombre(self):
        """Nombre de la figura."""
        return self.__nombre


class Circulo(Figura):
    """Representa un círculo.

    Extiende "Figura" añadiendo el radio y sobrescribe `area`
    para calcular el área del círculo.

    Atributos:
        radio: Radio del círculo, no puede ser negativo.
    """

    def __init__(self, nombre, radio):
        """Inicializa el círculo con un nombre y un radio.

        Argumentos:
            nombre: Nombre del círculo.
            radio: Radio del círculo.

        Raises:
            ValueError: Si el radio es negativo.
        """
        super().__init__(nombre)
        self.radio = radio

    @property
    def radio(self):
        """Radio del círculo."""
        return self.__radio

    @radio.setter
    def radio(self, valor):
        if valor < 0:
            raise ValueError("El radio debe ser positivo")
        self.__radio = valor

    def area(self):
        """Retorna el área del círculo (pi * (radio * radio))."""
        return (self.radio * self.radio) * 3.1416


class Rectangulo(Figura):
    """Representa un rectángulo.

    Extiende "Figura" añadiendo base y altura, y sobrescribe "area"
    para calcular el área del rectángulo.

    Atributos:
        base: Base del rectángulo.
        altura: Altura del rectángulo.
    """

    def __init__(self, nombre, base, altura):
        """Inicializa el rectángulo con nombre, base y altura.

        Argumentos:
            nombre: Nombre del rectángulo.
            base: Base del rectángulo.
            altura: Altura del rectángulo.
        """
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def area(self):
        """Retorna el área del rectángulo (base * altura)."""
        return self.base * self.altura


def calcular_area(figuras):
    """Imprime el nombre y el área de cada figura de una lista.

    Si un elemento no es instancia de "Figura", muestra un mensaje
    indicándolo.

    Argumentos:
        figuras (list): Lista de objetos a procesar.
    """
    for figura in figuras:
        if isinstance(figura, Figura):
            print(f"Figura: {figura.nombre} Area: {figura.area():.2f}")
        else:
            print("Esto no pertenece a la clase Figura")


def main():
    circulo1 = Circulo("Circulo 1", 7)
    circulo2 = Circulo("Circulo 2", 5)

    rectangulo1 = Rectangulo("Rectangulo 1", 5, 10)
    rectangulo2 = Rectangulo("Rectangulo 2", 12, 7)

    lista_figura = [circulo1, circulo2, rectangulo1, rectangulo2]

    calcular_area(lista_figura)

    help(Figura)
    help(Circulo)
    help(Rectangulo)


main()