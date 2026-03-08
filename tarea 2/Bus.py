class Bus: 
    def __init__(self, pasajeros, asientos):
        self.__pasajeros = pasajeros
        self.__asientos = asientos
        self.__pasaje = 0
    def cobrarpasaje(self, x):
        for i in range(x):
            self.__pasaje += 1.50
        
    def asientosdisponibles(self):
        return self.__asientos - self.__pasajeros
    def getpasajeros(self):
        return self.__pasajeros
    def getpasaje(self):
        return self.__pasaje
    
class Main:
    b1 = Bus(30, 50)
    b1.cobrarpasaje(b1.getpasajeros())
    print("pasajeros:", b1.getpasajeros(), "asientos disponibles:", b1.asientosdisponibles(), "pasaje:", b1.getpasaje())
