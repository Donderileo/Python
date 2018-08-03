#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor_1 = ['a','b','c']
vetor_2 = [1,2,3]
vetor_3 = [0,0,0]
intercalado = []

for i in range (0,3):
		intercalado.append(vetor_1[i])
		intercalado.append(vetor_2[i])
		intercalado.append(vetor_3[i])

print(intercalado)