vetores = []


def minha_soma(lista):
	soma = 0
	for i in range(len(lista)):
		soma += lista[i]
	return soma

for i in range(10):
	notas = [int(k) for k in input('Insira as 4 notas dos 10 alunos: ').split()]
	soma = minha_soma(notas)
	media = (soma) / len(notas)
	vetores.append(media)

aprovados = 0
for j in range(len(vetores)):
	if vetores[j] >= 7:
		aprovados += 1

print(f'A quantidade de alunos aprovados foi de: {aprovados}')
