num = int(input('Insira um número inteiro entre 1 e 10: '))

print(f'Tabuade de {num}: ')

for i in range(1,11):
	print(f'{num} X {i} = {num * i}')
