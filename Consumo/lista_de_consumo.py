def converte_valores(valores):
	for i in range(0,len(valores)):
		valores[i] = int(valores[i])
	for i in range(0,len(valores)):
		valores[i] = round(float(valores[i]) / (1024**2),2)
	return valores

def calculo_percentual(valores):
	x = sum(valores)
	perc = []
	for i in range(0,len(valores)):
		perc.append(round(((valores[i] * 100) / x),2))
	return perc  

nome_arquivo = "Base.txt" #nome_arquivo = input("Insira o nome do arquivo Base: ").
arquivo = open(nome_arquivo,"r")
dados_bruto = arquivo.read() #recebe todo o conteudo do arquivo.
arquivo.close()
lista_dividida = dados_bruto.split() #divide todo o conteudo em uma lista, ignorando os espaços e tabulações.

nomes = []
valores = []

for i in range (0,len(lista_dividida),2):
	nomes.append(lista_dividida[i])
for i in range(1,len(lista_dividida),2):
	valores.append(lista_dividida[i])

#cria uma lista para os nomes e uma para os valores.

valores = converte_valores(valores) #converte os valores de Bytes para MB / Str -> Int -> Float -> Arredonda com duas casas decimais
percentual = calculo_percentual(valores) #gera os percentuais, converte para string e adiciona o simbolo de %
media = round((sum(valores) / len(valores)),2) #calcula a média, já arredondando com 2 casas

arquivo = open("Relatorio.txt","w")
arquivo.write("ACME Inc.\t\tUso do espaço em disco pelos usuários\n------------------------------------------------------------------------\n")
arquivo.write("Nr\tUsuario\t\t\tEspaço Utilizado\t\t'%' do uso\n")

for i in range(0,len(nomes)):
	arquivo.write("{}\t{:<15}{:>8} MB {:>19}%".format(i,nomes[i],valores[i],percentual[i]))
	arquivo.write("\n")
arquivo.write("\n")
arquivo.write("Espaço total ocupado: {}\n".format(sum(valores)))
arquivo.write("Espaço medio ocupado: {}\n".format(media))