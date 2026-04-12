# clases.py
import math
from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self, c):
        self._color = c
    def getColor(self):
        return self._color
    @abstractmethod
    def getArea(self):
        pass    
    def mostrar(self):
        print(f"Figura [color={self._color}]")
    
class Redondo (Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.__radio = radio
    def getArea(self):
        return math.pi * self.__radio * self.__radio
    def mostrar(self):
        print (f"Redondo: radio {self.__radio}", end="") 
        super().mostrar()
class Cuadrado (Figura):
    def __init__(self, lado, color):
        super().__init__(color)
        self.__lado = lado
    def getArea(self):
        return self.__lado * self.__lado
    def mostrar(self):
        print(f"Cuadrado = lado {self.__lado}", end="")
        super().mostrar()
class Triangulo(Figura):
    def __init__(self, ladouno,ladodos,ladotres,color ):
        super().__init__(color)
        self.__lado1 = ladouno
        self.__lado2 = ladodos
        self.__lado3 = ladotres  
    def getArea(self):
        s = (self.__lado1 + self.__lado2 + self.__lado3)/2  
        return math.sqrt(s* (s-self.__lado1) * (s-self.__lado2)* (s-self.__lado3))
    def mostrar(self):
        print(f"Triangulo - lados = {self.__lado1, self.__lado2, self.__lado3}", end="")
        return super().mostrar()
    
class Main(): 
    c1 = Cuadrado (12, "Rojo")
    c2 = Cuadrado (15, "Morado")
    t1 = Triangulo (3, 2, 3, "Azul")
    t2 = Triangulo(3, 5, 6, "Rosa")    
    r1 = Redondo (3.14, "Blanco")
    r2 = Redondo (2, "Naranaja")
    figuras = [c1, c2, t1, t2, r1, r2]
    for f in figuras:
        f.mostrar()
    print()
    area_cuad = c1.getArea()
    area_tri = t1.getArea()
    if area_cuad > area_tri:
        print(f"El cuadrado de color {c1._color} tiene mayor área ({area_cuad:.2f}) que el triángulo ({area_tri:.2f}).")
    elif area_tri > area_cuad:
        print(f"El triángulo de color {t1._color} tiene mayor área ({area_tri:.2f}) que el cuadrado ({area_cuad:.2f}).")