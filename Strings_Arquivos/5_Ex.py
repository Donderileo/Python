arquivo = open("programa_5.txt","w") #Cria um arquivo para armazenar as notas e nomes
x = input("Insira o nome: ") #validar o primeiro nome

while(x != "s"):
	y = float(input("Insira a nota 1: "))
	z = float(input("Insira a nota 2: "))
	arquivo.write("%s   %.2f   %.2f\n"%(x,y,z))
	x = (input("Insira o nome: ")) #dar continuidade ao preenchimento ou não

arquivo.close()
