from statistics import mean
notas = input('Insira 4 números: ').split()

for i in range(len(notas)):
	notas[i] = int(notas[i])

print(f'As notas inseridas foram: {notas}')

media = mean(notas)
print(f'A média dessas 4 notas é de: {media}')
