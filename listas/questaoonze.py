import random

lista = []
lista2 = []
lista3 = []
for i in range(10):
	lista.append(random.randint(0, 101))
	lista2.append(random.randint(0, 101))
	lista3.append(random.randint(0, 101))
print(lista)
print(lista2)
print(lista3)

nueva_lista = []
for i in range(len(lista)):
	nueva_lista.append(lista[i])
	nueva_lista.append(lista2[i])
	nueva_lista.append(lista3[i])
print(nueva_lista)
