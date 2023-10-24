a = int(input('Insira um valor inteiro para o lado a: '))
b = int(input('Insira um valor inteiro para o lado b: '))
c = int(input('Insira um valor inteiro para o lado c: '))

if a > b + c or b > a + c or c > a + b:
	print('Esses valores não são válidos para a formação de um triângulo')

elif a == b and b == c:
	print('Triângulo equilátero')

elif a == b and b != c:
	print('Triângulo isósceles')

elif b == c and a != c:
	print('Triângulo isósceles')

elif a == c and b != c:
	print('Triângulo isósceles')

elif a != b and b != c:
	print('Triângulo escaleno')
