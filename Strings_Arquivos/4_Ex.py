def ehPalindromo(palavra):
	x = palavra[::-1] #Inverte a palavra(inicio,fim,intervalo de contagem)
	if(x == palavra): 
		return True
	return False

palavra = input("Insira a palavra: ")
print(ehPalindromo(palavra))