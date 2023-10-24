turno = input('Em que turno você estuda? Use M para matutino, V para Vespertino ou N para Noturno: ')

if turno == 'M' or turno == 'm':
	print('Bom dia!')

elif turno == 'V' or turno == 'v':
	print('Boa tarde!')

elif turno == 'N' or turno == 'n':
	print('Boa noite!')

else:
	print('Valor inválido!')
