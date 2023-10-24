salário = float(input('Insira quanto você recebe por hora: '))
horas = float(input('Insira quantas horas você trabalha por mês: '))

salário_bruto = (salário * horas) 

ir = salário_bruto - (salário_bruto * (0.89)) 
inss = salário_bruto - (salário_bruto * (0.98))
sindicato = salário_bruto - (salário_bruto * (0.95)) 
descontos = (ir + inss + sindicato)

salário_líquido = salário_bruto - descontos

print(f'O seu salário bruto foi de: {salário_bruto:.2f}')
print(f'O total descontado pro Imposto de Renda foi de: {ir:.2f}')
print(f'O total descontado para o INSS foi de: {inss:.2f}')
print(f'O total descontado para o Sindicato foi de: {sindicato:.2f}')
print(f'O seu salário líquido foi de: {salário_líquido:.2f}')
