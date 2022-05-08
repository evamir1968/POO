"""Objetos tienen atributos o propiedades -> Variables
   Funcionalidades o comportamientos -> Funciones o Métodos
   Encapsulamiento: Ocultar funcionamiento interno de objetos
   Ventajas: Modularización, reutilización, fácil incrementar 
   y mantener, fallos localizables y no afectanan al todo
   Clase es una plantilla
   
   Nota: en Python self = this de otros lenguajes,
   Si no lo escribimos en el método da type error en la 
   línea de la llamada. self da acceso a propiedades de la propia
   clase"""
   
class Persona():
	#Propiedades, caracteristicas o atributos:
	apellidos=""
	nombres=""
	edad=0
	despierta=False

	#Funcionalidades:
	def despertar(self):
		self.despierta=True 
		print("Buen día")

#Utilización de la clase Persona
persona1 = Persona() #Instanciamos clase Persona.
persona1.apellidos = "García Fuentes"
persona1.despertar() #Llamamos al método despertar.
print("Sr. ",persona1.apellidos)
print("Está despierta: ", persona1.despierta)

persona2 = Persona()
persona2.apellidos = "Moranles Montoya"
print("Sin llamar al método despiesta está dormida") 
print("Sr.", persona2.apellidos)
print("Está despierta: ", persona2.despierta)
