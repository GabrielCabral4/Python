num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira outro número inteiro: '))

intervalo = []

for i in range(num1 + 1, num2):
	intervalo.append(i)

soma = sum(intervalo)
print(f'A soma dos números presentes nesse intervalo equivale a: {soma}')
