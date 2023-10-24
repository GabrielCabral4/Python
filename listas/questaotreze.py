import random

medias = []
for media_mensal in range(12):
	medias.append(random.randint(20, 31))

soma = sum(medias)
media_anual = soma / 12
print(f'A média anual de temperatura ao longo do ano foi de: {media_anual:.1f}')

if medias[0] > media_anual:
	print(f'{medias[0]} - Janeiro')

elif medias[1] > media_anual:
	print(f'{medias[1]} - Fevereiro')

elif medias[2] > media_anual:
	print(f'{medias[2]} - Março')

elif medias[3] > media_anual:
	print(f'{medias[3]} - Abril')

elif medias[4] > media_anual:
	print(f'{medias[4]} - Maio')

elif medias[5] > media_anual:
	print(f'{medias[5]} - Junho')

elif medias[6] > media_anual:
	print(f'{medias[6]} - Julho')

elif medias[7] > media_anual:
	print(f'{medias[7]} - Agosto')

elif medias[8] > media_anual:
	print(f'{medias[8]} - Setembro')

elif medias[9] > media_anual:
	print(f'{medias[9]} - Outubro')

elif medias[10] > media_anual:
	print(f'{medias[10]} - Novembro')

elif medias[11] > media_anual:
	print(f'{medias[11]} - Dezembro')
