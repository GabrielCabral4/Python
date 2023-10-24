import random

idades = []
alturas = []

for num in range(30):
	idades.append(random.randint(12, 16))

for age in range(30):
	alturas.append(random.randint(155, 171))

soma_alturas = sum(alturas)
media_alturas = soma_alturas / 30

contador = 0
for i in range(len(idades)):
		if idades[i] > 13:
			if alturas[i] < media_alturas:
				contador += 1

print(f'A quantidade de alunos que tem mais de 13 anos e tem altura menor do que a média de todos os alunos é de: {contador}')
