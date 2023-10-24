nome = input('Insira seu nome: ')
idade = int(input('Insira sua idade: '))
salario = float(input('Insira seu salário: '))
sexo = input('Insira seu sexo usando "f" para feminino ou "m" para masculino: ')
estado = input('Insira seu estado civil usando "s" para solteiro(a), "c" para casado(a), "v" para viúvo(a) e "d" para divorciado(a): ')

for i in range(len(nome)):
	if len(nome) < 3:
		print('Nome inválido')
		nome = (input('Insira seu nome: '))

if idade < 0 or idade > 150:
	print('Idade inválida')
	idade = int(input('Insira sua idade: '))

if salario < 0:
	print('Salário inválido')
	salario = float(input('Insira seu salário: '))

for b in range(len(sexo)):
	if sexo != 'f' or sexo != "F" and sexo != 'm' or sexo != "M":
		print('Sexo inválido')
		sexo = input('Insira seu sexo usando "f" para feminino ou "m" para masculino: ')

for c in range(len(estado)):
	if estado != 'c' and estado != 'v' and estado != 'd' and estado != 's':
		print('Estado civil inválido')
		estado = ('Insira seu estado civil usando "s" para solteiro(a), "c" para casado(a), "v" para viúvo(a) e "d" para divorciado(a)')
