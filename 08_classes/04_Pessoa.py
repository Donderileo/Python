class Pessoa:
	def __init__(self, nome, idade, peso, altura): #Construtor
		self.nome = nome
		self.idade = idade
		self.peso = peso
		self.altura = altura
	def envelhecer(self): #Se idade for menor que 21 anos, crescer 0,5cm
		if(self.idade <= 21):
			self.idade += 1
			self.altura += 0.005
		else:
			self.idade +=1
	def imprime(self):
		print("Nome: " + self.nome)
		print("Idade: %d \nPeso: %d \nAltura: %.3f"% (self.idade,self.peso,self.altura))

x = Pessoa("Leo",19,60,1.80)
x.imprime()
x.envelhecer()
print("-----------")
x.imprime()
#Os outros metodos, são simples "engordar, emagrecer, crescer"
