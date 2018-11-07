arquivo = open("programa_5.txt","w")
x = input("Insira o nome: ")

while(x != "s"):
	y = float(input("Insira a nota 1: "))
	z = float(input("Insira a nota 2: "))
	arquivo.write("%s   %.2f   %.2f\n"%(x,y,z))
	x = (input("Insira o nome: "))

arquivo.close()
