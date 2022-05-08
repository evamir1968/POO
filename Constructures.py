"""Constructores y encapsulamiento, se pueden encapsular las pro-
piedades y los métodos poniendo delante doble guion bajo __, lo encap-
sulado sólo es accesible desde la clase a la que pertenece, para acceder
a ello lo podemos hacer con una algo público"""
class Curso():
	nombre = ""
	creditos = 0
	profesion = ""

	#Constructor de Python asigna estado inicial
	def __init__(self, nom,cre,pro):
		self.nombre = nom
		self.creditos = cre
		self.profesion = pro
		self.__imparticion = "Presencial" #Encapsulada

	def mostrarDatos(self): #Ej acceso a prop incluso encapsuladas
		dat = "nombre: {0} - créditos: {1} - modo de impartición: {2}"
		print(dat.format(self.nombre, self.creditos, self.__imparticion))
		docenteAsignido = self.__verificarDocente()
		if docenteAsignido:
			print("Existe Docente asignado")
		else:
			print("Docente no necesario por virtual")

	def __verificarDocente(self): #Encapsulada
		print("Se ha llamado a encapsulada")
		if self.__imparticion == "Presencial":
			return True
		else:
			return False
			
#Utlización de la clase y constructor.
curso1 = Curso("Matemáticas", 5, "Ingeniería Civil")
print(curso1.nombre)

curso2 = Curso("Lenguaje", 6, "Enfermería")
print("Nombre: " , curso2.nombre)
print("Créditos: " , curso2.creditos)
print("profesion: " , curso2.profesion)
print("Llamo a función mostrarDatos no encapsulada")
curso2.mostrarDatos()
