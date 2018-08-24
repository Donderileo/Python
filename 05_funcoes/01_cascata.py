#numeros em cascata
def cascata(num):
	for i in range(1,num+1):
		j = 0
		while(j != i):
			print("%d"%(i),end=" ")
			j += 1

		print("\n")

		
num = int(input("Insira o número da cascata: "))
cascata(num)
