#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = [1,2,3,4,5,6,7,8,9,10]
alturas = [21,22,23,24,25,26,27,28,29,30]
total = 0
media = sum(alturas)/len(alturas)

for i in range (0,10):
	if (alturas[i] < media):
		total += 1

print("O total de alunos com menos de %.2f de altura é %d"%(media,total))