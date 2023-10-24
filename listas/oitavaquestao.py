idade = input('Insira a idade de 5 pessoas: ').split()
altura = input('Agora insira a altura dessas 5 pessoas: ').split()

x = -1
for i in range(int(len(idade) / 2)):
	idade[i], idade[x] = idade[x], idade[i]
	x -= 1

print(idade)
