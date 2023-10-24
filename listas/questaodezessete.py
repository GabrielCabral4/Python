from statistics import mean

saltos = []
atleta = input('Insira o nome do atleta: ')

primeiro_salto = float(input('Insira a distância alcançada no primeiro salto: '))
segundo_salto = float(input('Insira a distância alcançada no segundo salto: '))
terceiro_salto = float(input('Insira a distância alcançada no terceiro salto: '))
quarto_salto = float(input('Insira a distância alcançada no quarto salto: '))
quinto_salto = float(input('Insira a distância alcançada no quinto salto: '))

saltos.append(primeiro_salto)
saltos.append(segundo_salto)
saltos.append(terceiro_salto)
saltos.append(quarto_salto)
saltos.append(quinto_salto)

media = mean(saltos)

print(f'Atleta: {atleta}')

print(f'Primeiro salto: {primeiro_salto} m')
print(f'Segundo salto: {segundo_salto} m')
print(f'Terceiro salto: {terceiro_salto} m')
print(f'Quarto salto: {quarto_salto} m')
print(f'Quinta salto: {quinto_salto} m')

print('Resultado final:')
print(f'Atleta: {atleta}')
print(f'Saltos: {primeiro_salto} - {segundo_salto} - {terceiro_salto} - {quarto_salto} - {quinto_salto}')
print(f'Média dos saltos: {media} m')
