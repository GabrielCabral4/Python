num = int(input('Insira um número inteiro: '))

resultado = 0
for i in range(num, 2, -1):
	resultado += (num) * (num - 1)

print(f'O fatorial desse número é {num}! = {resultado}')
