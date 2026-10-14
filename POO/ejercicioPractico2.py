class Figura:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def area(self):
        return 0
    
    @property
    def nombre(self):
        return self.__nombre
    
class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio
        
    @property
    def radio(self):
        return self.__radio
        
    @radio.setter
    def radio(self, valor):
        if valor < 0:
            raise ValueError("El radio debe ser positivo")
        self.__radio = valor
    
    def area(self):
        return (self.radio * self.radio) * 3.1416
    
class Rectangulo(Figura):
    def __init__(self, __nombre, base, altura):
        super().__init__(__nombre)
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
def calcular_area(figuras):
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
main()


