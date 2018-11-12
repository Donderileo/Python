class Tamagotchi():

	def __init__(self,nome):
		self.nome = nome
		self.fome = 1
		self.saude = 10
		self.idade = 0

	def getSaude(self):
		return self.saude
	
	def getFome(self):
		return self.fome

	def getHumor(self):
   		return self.getSaude() * self.getFome()

bixo = Tamagotchi("X")
print(bixo.getHumor())