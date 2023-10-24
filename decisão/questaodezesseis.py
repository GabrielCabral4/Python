a = float(input('Insira um a para uma função do segundo grau: '))
if a == '0':
	print('A equação não é do segundo grau')

b = float(input('Insira um b para uma função do segundo grau: '))
c = float(input('Insira um c para uma função do segundo grau: '))

delta = (b ** 2) - 4 * a * c
raíz1 = (-b + delta ** (1/2)) / (2 * a)
raíz2 = (-b - delta ** (1/2)) / (2 * a)

if delta < 0:
	print('A equação não possui raízes reais')

elif delta == 0:
	print(f'A equação possui apenas uma raíz real:{raíz1}')

elif delta > 0:
	print(f'A equação possui duas raízes reais: {raíz1} e {raíz2}')
