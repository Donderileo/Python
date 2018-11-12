def cria_arquivo(n):
	aux = "a"
	for i in range(0,n):
		arq = open(aux,'w')
		arq.close()
		aux += "a"

n = int(input("Insira um numero: "))
cria_arquivo(n) #Cria varios arquivos com nomes = {a,aa,aaa...}