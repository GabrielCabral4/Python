salario = float(input('Insira o seu salário: '))

if salario <= 280.00:
	print(f'O seu salário atual é de R$ {salario:.2f}')
	print(f'O seu percentual de aumento é 20%')
	salario_a1 = ((salario * 20) / 100) + salario
	print(f'O aumento no seu salário é de R$ {salario_a1 - salario:.2f}')
	print(f'O seu novo salário é de: R$ {salario_a1:.2f}')

elif 280.00 < salario < 700:
	print(f'O seu salário atual é de R$ {salario:.2f}')
	print(f'O seu percentual de aumento é de 15%')
	salario_a2 = ((salario * 15) / 100) + salario
	print(f'O aumento no seu salário é de R$ {salario_a2 - salario:.2f}')
	print(f'O seu novo salário é de: R$ {salario_a2:.2f}')

elif 700 < salario < 1500:
	print(f'O seu salário atual é de R$ {salario:.2f}')
	print(f'O seu percentual de aumento é de 10%')
	salario_a3 = ((salario * 10) / 100) + salario
	print(f'O aumento no seu salário é de R$ {salario_a3 - salario:.2f}')
	print(f'O seu novo salário é de: R$ {salario_a3:.2f}')

elif salario > 1500:
	print(f'O seu salário atual é de R$ {salario:.2f}')
	print(f'O seu percentual de aumento é de 5%')
	salario_a4 = ((salario * 5) / 100) + salario
	print(f'O aumento no seu salário é de R$ {salario_a4 - salario:.2f}')
	print(f'O seu novo salário é de: R$ {salario_a4:.2f}')
