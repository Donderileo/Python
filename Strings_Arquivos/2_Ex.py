'''
Faça uma função que recebe como entrada uma string estruturada na forma “nome,
nota”, a função retorna dois valores: o nome e a nota convertida para o tipo float.
Por exemplo, para a string “Eduardo Silva, 8.5” a função retorna “Eduardo Silva” e
também o valor 8.5.
'''
def separa(nome):
	x = nome.split(",")
	nota = float(x[1])
	name = x[0]
	return name,nota

h = "Leonardo, 8.5"
tupla = separa(h)
print("Nome: %s, Nota: %.2f"%(tupla[0],tupla[1]))