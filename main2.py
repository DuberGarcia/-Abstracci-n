
class Asociado():
    
    def __init__(self,nombre,es_activo):
        self.nombre=nombre
        self.es_activo=es_activo

    def crear_cuenta(self):
        print(F"Cuenta de asociado dependiente {self.nombre} creada")

    def imprimir_asociado(self):
        print(f"nombre: {self.nombre} estado: {self.estado}")

class Dependiente():

    def __init__(self,nombre,es_activo):
        self.nombre=nombre
        self.es_activo=es_activo

    def crear_cuenta(self):
        print(F"Cuenta de asociado dependiente {self.nombre} creada")
    

class Independiente():

    def __init__(self,nombre,es_activo):
        self.nombre=nombre
        self.es_activo=es_activo

    def crear_cuenta(self):
        print(F"Cuenta de asociado independiente {self.nombre} creada")


asocia1=Dependiente("juan",True)
asocia2=Independiente("juan",True)
asocia3=Dependiente("juan",True)
asocia4=Asociado("juan",True)
asocia5=Dependiente("juan",True)

asociados = [asocia1,asocia2,asocia3,asocia4,asocia5]

for aso in asociados:
    aso.crear_cuenta()