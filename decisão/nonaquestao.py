n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 > n2 and n1 > n3 and n2 > n3:
	print(f'A ordem decrescente dos números é: {n1}, {n2}, {n3}')

elif n2 > n1 and n2 > n3 and n1 > n3:
	print(f'A ordem decrescente dos números é: {n2}, {n1}, {n3}')

elif n3 > n1 and n3 > n2 and n1 > n2:
	print(f'A ordem decrescente dos números é: {n3}, {n1}, {n2}')

elif n1 > n2 and n1 > n3 and n3 > n2:
	print(f'A ordem decrescente dos números é: {n1}, {n3}, {n2}')

elif n2 > n1 and n2 > n3 and n3 > n1:
	print(f'A ordem decrescente dos números é {n2}, {n3}, {n1}')

elif n3 > n1 and n3 > n2 and n2 > n1:
	print(f'A ordem descrescente dos números é {n3}, {n2}, {n1}')
