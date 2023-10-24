data = input('Insira uma data no formato dd/mm/aaaa: ').split('/')

dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

cond = dia in range(1, 32) and mes == 1 or mes in range(3, 13) or dia in range(1, 29) and mes == 2

if cond:
	print('Data válida')

else:
	print('Data inválida')
