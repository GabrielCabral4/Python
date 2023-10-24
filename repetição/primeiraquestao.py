nota = int(input('Insira uma nota entre 0 e 10: '))

for i in range(nota):
	if 0 <= nota <= 10:
		print('A nota inserida é válida')
		break
	else:
		print('A nota inserida é inválida')
		nota = int(input('Insira uma nota entre 0 e 10: '))
