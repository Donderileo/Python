'''
class Bola:
	def __init__(self,color,circunf,material):
		self.color = color
		self.circunf = circunf
		self.material = material
	def trocaCor(self,new_color):
		self.color = new_color
	def mostraCor(self):
		print(self.color)

x = Bola("Vermelho","3","Aço")
x.mostraCor()
x.trocaCor("Preto")
x.mostraCor()
'''
'''
class Quadrado:
	def __init__(self,lado):
		self.lado = lado
	def mudar_lado(self,new_lado):
		self.lado = new_lado
	def getLado(self):
		print("Lado: " + str(self.lado))
	def area(self):
		area = (self.lado) * (self.lado)
		print("Area: " + str(area))

x = Quadrado(5)
x.getLado()
x.mudar_lado(3)
x.getLado()
x.area()
'''