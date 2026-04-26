class Libro:
    def __init__(self, nombre, autor, año):
        self.__nombre = nombre
        self.__autor = autor
        self.__año = año 
    
    def getNombre(self):
        return self.__nombre
    
    def getAutor(self):
        return self.__autor
    
    def getAño(self):
        return self.__año

    def __str__(self):
        return f"Libro: {self.__nombre}, Autor: {self.__autor}, Año: {self.__año}"

class Biblioteca :
    def __init__(self, nombre):  
        self.__nombre = nombre
        self.__libros = []
    def getNombre(self):
        return self.__nombre
    
    def agregarlibro(self, libro):
        if libro not in self.__libros:
            self.__libros.append(libro)
        
    def mostrarLibro(self):
        print("Biblioteca: ", self.__nombre)
        if len(self.__libros) == 0:
            print("no hay libros")
        else:
            for i in self.__libros:
                print(i)
    def buscarLibro(self, nombre):
        for i in self.__libros:
            if i.getNombre() == nombre:
                print("Libro encontrado:")
                print(i)
                return
        print("Libro no encontrado")

    def cantidadLibros(self):
        return len(self.__libros)
    
l1 = Libro("100 años de soledad", "Garcia Marquez", 1978)
l2 = Libro("El amor en los tiempos de colera", "Garcia Marquez", 1980) 
l3 = Libro("El señor de los anillos", "J.R.R Tolkien", 1960)
l4 = Libro("Las Aventuras de Colita Dorada", "Hugo Villanueva", 1993)

b1 = Biblioteca("Biblioteca Nacional de España")
b2 = Biblioteca("Biblioteca de Alejandria")
#b
b1.agregarlibro(l1)
b1.agregarlibro(l2)

b2.agregarlibro(l3)
b2.agregarlibro(l4)

b1.mostrarLibro()
b2.mostrarLibro()
#c
b1.buscarLibro("100 años de soledad")
#d
print("Biblioteca con mas libros: ")
if b1.cantidadLibros() > b2.cantidadLibros():
    print(b1.getNombre())
elif b1.cantidadLibros() < b2.cantidadLibros():
    print(b2.getNombre())
else:
    print("Tienen la misma cantidad de libros")
    print(b1.getNombre())
    print(b2.getNombre())