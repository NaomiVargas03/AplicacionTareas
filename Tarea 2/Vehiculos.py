#vehiculos.py
#Nicole Naomi Vargas Rodríguez, Tarea 2, segundo semestre.

#Para utilizar el método de abstracción.
from abc import ABC, abstractmethod  
class flota_vehiculos(ABC):
    @abstractmethod

#Presenta un error si una subclase no utiliza este método.
    def Obtener_informacion(self): 
        pass                  

#Se utiliza para iniciar la superclase vehiculo.
class vehiculo:           
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio= precio
    
    def Obtener_informacion(self):
       return f"Marca del vehiculo: {self.marca}, modelo: {self.modelo}, año del vehiculo: {self.año} y precio: {self.precio}"

#Para iniciar la subclase carro
class Carro(vehiculo):
    def __init__(self, tipo1, marca, modelo, año, precio):
        super().__init__(marca, modelo, año, precio) #Se utiliza para acceder a los atributos de la superclase
        self.tipo1 = tipo1

    def Obtener_informacion(self):
       return f"Tipo: {self.tipo1}, Marca del coche: {self.marca}, modelo: {self.modelo}, año del vehiculo: {self.año}  y precio por día: {self.precio}"


#Para iniciar la subclase camión
class Camion(vehiculo):
    def __init__(self, tipo, marca, modelo, año, precio): #Se utiliza para acceder a los atributos de la superclase
        super().__init__(marca, modelo, año, precio)
        self.tipo = tipo
    
    def mostrar_informacion(self):
       return f"Tipo: {self.tipo}, Marca del auto: {self.marca}, modelo: {self.modelo}, año del vehiculo: {self.año} y precio por día: {self.precio}"
    

#Subclase carro.
carro= Carro("Carro", "Toyota", "corolla", "2024", "$700")
print(f"◑ Información obtenida: {carro.Obtener_informacion()}")

#Subclase camión.
camion= Camion("Camión", "Ford", "F-250 Super Duty", "2024", "$1100")
print(f"◑ Información obtenida: {camion.Obtener_informacion()}")  


print()
print()
print("(Profe, no sé por qué no se imprime lo del tipo del camión pero del carro sí T-T)")