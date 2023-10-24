answers = []

answer1 = input('Telefonou para a vítima? ')
answer2 = input('Esteve no local do crime? ')
answer3 = input('Mora perto da vítima? ')
answer4 = input('Devia para a vítima? ')
answer5 = input('Já trabalhou com a vítima? ')

answers.append(answer1)
answers.append(answer2)
answers.append(answer3)
answers.append(answer4)
answers.append(answer5)

contador = 0
for answer in range(len(answers)):
	if answers[answer] == 'sim' or answers[answer] == 'Sim':
		contador += 1

if contador < 2:
	print('Inocente.')

elif contador == 2:
	print('Suspeita.')

elif contador == 3 or contador == 4:
	print('Cúmplice.')

elif contador == 5:
	print('Assasino.')
