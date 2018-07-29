#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver
number  = int(input("Qual tabuada deseja ver?: "))
for n in range(0,11):

	print("%d x %d = %d"%(number,n,number*n))