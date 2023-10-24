vetor = input('Insira uma lista de 20 números inteiros: ').split()

pares = []
impares = []

for i in range(len(vetor)):
	if int(vetor[i]) % 2 == 0:
		pares.append(vetor[i])

	elif int(vetor[i]) % 2 != 0:
		impares.append(vetor[i])

print(f'A lista de 20 vetores que você inseriu foi: {vetor}')
print(f'Desses vetores, os pares são: {pares}')
print(f'Desses vetores, os impares são: {impares}')

