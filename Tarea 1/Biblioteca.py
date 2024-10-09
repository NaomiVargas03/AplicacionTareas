#Biblioteca.py
#Nicole Naomi Vargas Rodríguez, Tarea 1, segundo semestre.

#Para utilizar el método de abstracción.
from abc import ABC, abstractmethod  
class MaterialBiblioteca(ABC):
    @abstractmethod

#Presenta un error si una subclase no utiliza este método.
    def Obtener_informacion(self): 
        pass                  

#Se utiliza para iniciar la subclase Periodico.
class Periodico(MaterialBiblioteca):           
    def __init__(self, fechaPublicacion, Imprenta):
        self.fechaPublicacion = fechaPublicacion
        self.Imprenta = Imprenta
    
    def Obtener_informacion(self):
       return f"Fecha de publicación: {self.fechaPublicacion}, imprenta: {self.Imprenta}"

#Se utiliza para iniciar la subclase Revista.
class Revista(MaterialBiblioteca):
    def __init__(self, NombreRevista, AñoPublicacion, Creador):
        self.NombreRevista = NombreRevista
        self.AñoPublicacion = AñoPublicacion
        self.Creador = Creador
    
    def Obtener_informacion(self):
        return f"Nombre de la revista: {self.NombreRevista}, nombre del creador: {self.Creador}, año de publicación: {self.AñoPublicacion}"

#Se utiliza para iniciar la subclase Libro.
class Libro(MaterialBiblioteca):
    def __init__(self, Titulo, Autor, Año_publicacion):
        self.Titulo = Titulo
        self.Autor = Autor
        self.Año_publicacion = Año_publicacion

    def Obtener_informacion(self):
        return f"Nombre del libro: {self.Titulo}, nombre del autor: {self.Autor}, año de publicación: {self.Año_publicacion}"
    

#Para crear instancias de cada una de las subclases.

#Subclase Periodico.
periodico = Periodico("23 de marzo de 2024", "La nación" ) 
print(f"◑ Información obtenida del periódico: {periodico.Obtener_informacion()}")

#Subclase Revista.
revista = Revista("VOGUE", 1892, "Arthur Baldwin Turnure")
print(f"◑ Información obtenida de la revista: {revista.Obtener_informacion()}")

#Subclase Libro.
libro = Libro("El principito", "Antoine de Saint-Exupéry", 1943 )
print(f"◑ Información obtenida del libro: {libro.Obtener_informacion()}")