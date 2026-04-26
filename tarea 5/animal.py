class Animal:
    def __init__(self, nombre, edad, dueño):
        self.__nombre = nombre 
        self.__edad = edad
        self.__dueño = dueño
    
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getNombreDuenio(self):
        return self.__dueño
    
    def __str__(self):
        return f"{self.__nombre}, Edad: {self.__edad}, Dueño: {self.__dueño}"


class Perro(Animal):
    def __init__(self, nombre, edad, dueño, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, dueño)
        self.__requiereBosal = requiereBosal
        self.__ladraFuerte = ladraFuerte
    
    def __str__(self):
        return f"Perro: {super().__str__()}, Bosal: {self.__requiereBosal}, Ladra fuerte: {self.__ladraFuerte}"


class Gato(Animal):
    def __init__(self, nombre, edad, dueño, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, dueño)
        self.__cazaRatones = cazaRatones
        self.__tomaLeche = tomaLeche
    
    def getTomaLeche(self):
        return self.__tomaLeche

    def __str__(self):
        return f"Gato: {super().__str__()}, Toma leche: {self.__tomaLeche}"    


class CentroVeterinario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__perros = []
        self.__gatos = []
    
    def addPerro(self, p):
        self.__perros.append(p)

    def addGato(self, g):
        self.__gatos.append(g)

    #B
    def ordenarPerros(self):
        self.__perros.sort(key=lambda p: (p.getEdad(), p.getNombreDuenio(), p.getNombre()))
    
    #  C
    def ordenarGatos(self):
        self.__gatos.sort(key=lambda g: (
            not g.getTomaLeche(),   
            -g.getEdad(),           
            g.getNombre()           
        ))


    def mostrar(self):
        print("\nCentro:", self.__nombre)

        print("Perros")
        for p in self.__perros:
            print(p)

        print("Gatos")
        for g in self.__gatos:
            print(g)

    # Inciso D
    def verificarDuenios(self):
        conteo = {}

        for p in self.__perros:
            d = p.getNombreDuenio()
            conteo[d] = conteo.get(d, 0) + 1

        for g in self.__gatos:
            d = g.getNombreDuenio()
            conteo[d] = conteo.get(d, 0) + 1

        print("\nDueños con más de un animal:")
        for d in conteo:
            if conteo[d] > 1:
                print(d, "tiene", conteo[d], "animales")





c1 = CentroVeterinario("Centro 1")
c2 = CentroVeterinario("Centro 2")


p1 = Perro("Choco", 4, "Luis", True, True)
p2 = Perro("Manchas", 3, "Mario", False, False)

g1 = Gato("Karen", 2, "Lucia", True, True)
g2 = Gato("Melvin", 4, "Ariel", False, False)

c1.addPerro(p1)
c1.addPerro(p2)
c1.addGato(g1)
c1.addGato(g2)


p3 = Perro("Princesa", 6, "Raul", True, False)
p4 = Perro("Leia", 2, "Fabiola", False, True)

g3 = Gato("Kira", 3, "Raul", True, False)
g4 = Gato("Azrael", 1, "Fabio", False, True)

c2.addPerro(p3)
c2.addPerro(p4)
c2.addGato(g3)
c2.addGato(g4)


c1.ordenarPerros()
c1.ordenarGatos()

c2.ordenarPerros()
c2.ordenarGatos()


c1.mostrar()
c1.verificarDuenios()

c2.mostrar()
c2.verificarDuenios()