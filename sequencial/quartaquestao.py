print('Digite abaixo as notas dos 4 bimestres:')

nota_1 = float(input('primeiro bimestre = '))
nota_2 = float(input('segundo bimestre = '))
nota_3 = float(input('tereceiro bimestre = '))
nota_4 = float(input('quarto bimestre = '))

média = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'A média dos 4 bimestres foi {média:.1f}')
