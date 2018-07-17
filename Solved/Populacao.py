'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B
'''

A = 80000
B = 200000
anos = 0
while (B > A):
	A = A * 1.03
	B = B * 1.015
	anos = anos + 1

print("População A: %d \nPopulação B: %d \nAnos necessarios: %d"% (A,B,anos))

'''
# Define os valores de populacao e crescimento
populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015

# Realiza calculo de anos
ano = 1
while (populacaoA <= populacaoB):
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    ano += 1

# Imprime o resultado
print ('Serao necessarios', ano, 'anos para que a populacao do pais A'\
    ' ultrapasse a populacao do pais B')
'''