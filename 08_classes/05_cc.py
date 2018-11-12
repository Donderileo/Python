class ContaCorrente():
	def __init__(self,numero,nome,saldo = 0): #Construtor com valor default para saldo
		self.numero = numero
		self.nome = nome
		self.saldo = saldo
	def alterarNome(self, new_nome):
		self.nome = new_nome
	def deposito(self, valor):
		self.saldo += valor
	def saque(self, valor):
		self.saldo -= valor
	def imprime(self): #Função que imprime os valores do objeto 
		print("Numero: {}\nNome: {} \nSaldo: {}".format(self.numero,self.nome, self.saldo))

x = ContaCorrente(555, "X")
y = ContaCorrente(333, "Y", 500)
x.imprime()
y.imprime()
print("--------")
x.deposito(50)
x.imprime()
