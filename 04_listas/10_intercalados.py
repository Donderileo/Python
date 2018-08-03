#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vetor_1 = ['a','b','c']
vetor_2 = [1,2,3]
vetor_3 = []
k = 0
j = 0
for i in range (1,7):
		if (i%2 == 0):
			vetor_3.append(vetor_1[k])
			k += 1
		else:
			vetor_3.append(vetor_2[j])
			j += 1
print(vetor_3)
