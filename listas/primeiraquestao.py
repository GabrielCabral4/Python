lista = input('Insira uma lista de inteiros: ').split()

for i in range(len(lista)):
	lista[i] = int(lista[i])

print(lista)
