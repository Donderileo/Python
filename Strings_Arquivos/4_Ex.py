def ehPalindromo(palavra):
	x = palavra[::-1]
	if(x == palavra):
		return True
	return False

palavra = input("Insira a palavra: ")
print(ehPalindromo(palavra))