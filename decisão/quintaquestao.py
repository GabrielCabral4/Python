nota_1 = float(input('Insira sua primeira nota parcial: '))
nota_2 = float(input('Insira sua segunda nota parcial: '))

if (nota_1 + nota_2) / 2 == 10:
	print('Aprovado com Distinção') 

elif (nota_1 + nota_2) / 2 >= 7:
	print('Aprovado')

elif (nota_1 + nota_2) / 2 < 7:
	print('Reprovado')
