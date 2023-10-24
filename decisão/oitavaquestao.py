produto1 = float(input('Insira o preço do primeiro produto: '))
produto2 = float(input('Insira o preço do segundo produto: '))
produto3 = float(input('Insira o preço do terceiro produto: '))

if produto1 < produto2 and produto1 < produto3:
	print('Você deve comprar o primeiro produto.')

elif produto2 < produto1 and produto2 < produto3:
	print('Você deve comprar o segundo produto.')

elif produto3 < produto1 and produto3 < produto1:
	print('Você deve comprar o terceiro produto.')
