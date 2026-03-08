class Minecraft:
    def __init__(self):
        self.__jugadores = []
        self.__diamantes = []

    def agregarjugador(self, j):
        self.__jugadores.append(j)
                
    def stacks(self, d):
        s = 0 
        while (d >0):  
            if (d >= 64): 
                s += 1
            d -= 64
        return s
    
    def agregarDiamante(self, d):
        self.__diamantes.append(d)

    def totalDiamantes(self):
        t = 0
        for d in self.__diamantes:
            t += d
        return t
    
    def getJugadores(self):
        return self.__jugadores
    
    def maxdiamantes(self):
        max=0
        for i in (0, len(self.__diamantes)-1):
           if self.__diamantes[i] > max:
                max = self.__diamantes[i]
        return self.__jugadores[i], max        
                           
class Main:
    j1 = Minecraft()
    j1.agregarjugador("juan")
    j1.agregarDiamante(65)

    j1.agregarjugador("pedro")    
    j1.agregarDiamante(128)

    j1.agregarjugador("maria")
    j1.agregarDiamante(32)

    j1.agregarjugador("ana")
    j1.agregarDiamante(16)

    j1.agregarjugador("luis")
    j1.agregarDiamante(64)

    j1.agregarjugador("carlos")
    j1.agregarDiamante(128)

    j1.agregarjugador("lucia")
    j1.agregarDiamante(16)

    j1.agregarjugador("sofia")
    j1.agregarDiamante(32)

    j1.agregarjugador("diego")
    j1.agregarDiamante(64)

    j1.agregarjugador("laura")
    j1.agregarDiamante(128)

    print("jugador con mas diamantes:", j1.maxdiamantes())
    print ("total de diamantes:", j1.totalDiamantes())
    
    
    