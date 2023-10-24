n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))
n3 = int(input('Insira mais um número inteiro: '))

if n1 > n2 and n2 > n3:
	print(f'{n1} é o maior número e {n3} é o menor número')

elif n2 > n1 and n1 > n3:
	print(f'{n2} é o maior número e {n3} é o menor número')

elif n3 > n1 and n1 > n2:
	print(f'{n3} é o maior número e {n2} é o menor número')

elif n1 > n3 and n3 > n2:
	print(f'{n1} é o maior número e {n2} é o menor número')

elif n2 > n3 and n3 > n1:
	print(f'{n2} é o maior número e {n1} é o menor número')

elif n3 > n2 and n2 > n1:
	print(f'{n3} é o maior número e {n1} é o menor número')
