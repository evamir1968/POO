"""Los métodos GET Y SET sirven para leer y modificar
propiedades encapsuladas de una clase, de otra manera no 
serían accesibles desde fuera"""
class Cuenta():
	
	def __init__(self, pro, sal, mon):
		self.__propietario = pro
		self.__saldo = sal
		self.__moneda = mon

	#Getters (Métodos GET)
	def get_Saldo(self):
		return self.__saldo		

	def get_Propietario(self):
		return self.__propietario

	def get_Moneda(self):
		return self.__moneda

	#SETTERS (Métodos SET)
	def set_Moneda(self, moneda):
		self.__moneda = moneda


cuenta1=Cuenta("Oscar García", 15000,"€")
print(cuenta1.get_Propietario(), cuenta1.get_Saldo(), cuenta1.get_Moneda())
cuenta1.set_Moneda("$")
print(cuenta1.get_Propietario(), cuenta1.get_Saldo(), cuenta1.get_Moneda())