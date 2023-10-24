user = input('Insira seu nome de usuário: ')
senha = input('Insira sua senha: ')

for i in range(len(user)):
	for j in range(len(senha)):
		if user == senha:
			print('Erro. Seu usuário não pode ser igual à sua senha')
			user = input('Insira seu nome de usuário: ')
			senha = input('Insira sua senha: ')


