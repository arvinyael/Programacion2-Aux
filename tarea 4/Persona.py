class Persona: 
    def __init__(self, nombre, carnet, edad):
        self._nombre = nombre
        self._carnet = carnet
        self._edad = edad

    def __str__(self):
        return f"nombre:  {self._nombre}; carnet: {self._carnet}; edad: {self._edad}"        
    
class Estudiante (Persona): 
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.__matricula = matricula
        self.__carrera = carrera
    
    def __str__(self):
        return super().__str__() + f"matricula: {self.__matricula}; carrera: {self.__carrera}"
    
    def getEdad(self): 
        return self._edad
    
    def mismacarrera (self, otro): 
        return self.__carrera == otro.__carrera 
                
class Docente (Persona): 
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.__antiguedad = antiguedad
        self.__sueldo = sueldo

    def __str__(self):
        return super().__str__() + f"antiguedad: {self.__antiguedad}; sueldo: {self.__sueldo}"
    
    def getEdad(self): 
        return self._edad
    
class Main(): 
    e1 = Estudiante("Juan", 120483, 20, 1886463, "Informatica")
    e2 = Estudiante("Marco", 12345, 18, 1886531, "Matemática")
    d1 = Docente("Felipez", 2234235, 45, 20, 20000000)
    print(e1.__str__)
    print(e2.__str__)
    print(d1.__str__)

    for i, e in enumerate([e1, e2], 1):
        if e.getEdad() == d1.getEdad():
            print(f"Estudiante {i} ({e._nombre}) tiene la misma edad que el docente.")
        else:
            print(f"Estudiante {i} ({e._nombre}) tiene edad distinta a la del docente.")
            
    if (e1.mismacarrera(e2)): 
        print(f"{e1._nombre} y {e2._nombre} estan en la misma carrera")
    else: print(f"{e1._nombre} y {e2._nombre} NO estan en la misma carrera")
    