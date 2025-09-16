from abc import ABC,abstractmethod

class Asociado(ABC):
    
    def __init__(self,nombre,es_activo):
        self.nombre=nombre
        self.es_activo=es_activo

    @abstractmethod
    def crear_cuenta(self):
        pass

    def imprimir_asociado(self):
        print(f"nombre: {self.nombre} estado: {self.estado}")

class Dependiente(Asociado):

    def crear_cuenta(self):
        print(F"Cuenta de asociado dependiente {self.nombre} creada")
    

class Independiente(Asociado):

    def crear_cuenta(self):
        print(F"Cuenta de asociado independiente {self.nombre} creada")


asociado1:Asociado = Dependiente("duber",True)

asociado2:Asociado = Independiente("santiago",True)

asociado1.crear_cuenta()
asociado2.crear_cuenta()