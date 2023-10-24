a = int(input('Insira o tamanho da população A: '))
b = int(input('Insira o tamanho da população B: '))
ano = 0

while a <= b:
		a = (a * 1.03)
		b = (b * 1.015)
		ano += 1

print(f'Foram necessários {ano} anos para que A ultrapassasse ou igualasse B')
