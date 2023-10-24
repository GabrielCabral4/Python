área = float(input('Insira o tamanho da área total a ser pintada em metros quadrados: '))

tinta = (área / 3)

latas = tinta / 18 
    
if tinta < 18: 
    print('Você precisará de 1 lata de tinta, que custa 80 reais')

