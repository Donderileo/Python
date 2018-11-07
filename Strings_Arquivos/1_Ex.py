'''Faça uma função que recebe o nome, idade e endereço de uma pessoa. A função usa
essas informações para criar uma nova string, estruturada da seguinte forma:
“<<nome>> possui <<idade>> anos e mora na rua <<endereço>>”
A função retorna a string criada.'''
def cria_string(nome,idade,endereco):
	aux = nome + " possui "
	aux += idade + " anos e mora em "
	aux += endereco
	return aux

nome = "Leo"
idade = "19"
endereco = "São Carlos"
print(cria_string(nome,idade,endereco))