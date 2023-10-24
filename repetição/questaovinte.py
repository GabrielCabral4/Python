resultado = 0
for i in range(15, 2, -1):
	num = int(input('Insira um número inteiro: '))
	if num < 16:
		resultado += (num) * (num - 1)
		print(f'O fatorial desse número é {num}! = {resultado}')
