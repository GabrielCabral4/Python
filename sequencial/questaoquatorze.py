peso = float(input('Informe quantos quilogramas de peixe João conseguiu pescar: '))

if peso > 50:
    excesso = peso - 50
    multa = (peso - 50) * 4 
    print(f'João conseguiu pescar {peso}kg de peixes, seu excesso foi de {excesso}, e a multa para esse excesso foi de {multa}')
else: 
    print('João não precisou pagar multa pois não teve excesso de peso!')

