nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))

media = ((nota1 + nota2) / 2)

if 9 <= media <= 10:
	print(f'Média: {media}')
	print('A')
	print('Aprovado')

elif 7.5 <= media < 9:
	print(f'Média: {media}')
	print('B')
	print('Aprovado')

elif 6 <= media < 7.5:
	print(f'Média: {media}')
	print('C')
	print('Aprovado')

elif 4 <= media < 6:
	print(f'Média: {media}')
	print('D')
	print('Reprovado')

elif media < 4:
	print(f'Média: {media}')
	print('E')
	print('Reprovado')

