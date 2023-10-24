hora = int(input('Insira o valor da sua hora de trabalho: '))
hora_mes = int(input('Insira a quantidade de horas que você trabalha por mês: '))

salario_bruto = float(hora * hora_mes)
inss = (0.10 * salario_bruto)
fgts = (0.11 * salario_bruto)


if salario_bruto <= 900:
	print(f'Salário Bruto: ({hora} * {hora_mes}) = R${salario_bruto}')
	print('Isento de desconto do imposto de renda')
	print(f'O seu imposto destinado ao inss vale: R${inss}')
	print(f'O seu imposto destinado ao fgts vale: R${fgts}')
	ir = 0
	impostos = (inss + ir)
	salario_liquido = (salario_bruto - impostos)
	print(f'O total dos seus descontos foi de: {impostos}')
	print(f'O seu salário líquido vale: {salario_liquido}')

elif salario_bruto <= 1500:
	print(f'Salário Bruto: ({hora} * {hora_mes}) = R${salario_bruto}')
	print('Imposto de renda: 5%')
	print(f'O seu imposto destinado ao inss vale: R${inss}')
	print(f'O seu imposto destinado ao fgts vale: R${fgts}')
	ir = (0.05 * salario_bruto)
	impostos = (inss + ir)
	salario_liquido = (salario_bruto - impostos)
	print(f'O total dos seus descontos foi de: {impostos}')
	print(f'O seu salário líquido vale: {salario_liquido}')

elif salario_bruto <= 2500:
	print(f'Salário Bruto: ({hora} * {hora_mes}) = R${salario_bruto}')
	print('Imposto de renda: 10%')
	print(f'O seu imposto destinado ao inss vale: R${inss}')
	print(f'O seu imposto destinado ao fgts vale: R${fgts}')
	ir = (0.10 * salario_bruto)
	impostos = (inss + ir)
	salario_liquido = (salario_bruto - impostos)
	print(f'O total dos seus descontos foi de: {impostos}')
	print(f'O seu salário líquido vale: {salario_liquido}')

elif salario_bruto > 2500:
	print(f'Salário Bruto: ({hora} * {hora_mes}) = R${salario_bruto}')
	print(f'Imposto de renda: 20%')
	print(f'O seu imposto destinado ao inss vale: R${inss}')
	print(f'O seu imposto destinado ao fgts vale: R${fgts}')
	ir = (0.20 * salario_bruto)
	impostos = (inss + ir)
	salario_liquido = (salario_bruto - impostos)
	print(f'O total dos seus descontos foi de: {impostos}')
	print(f'O seu salário líquido vale: {salario_liquido}')

