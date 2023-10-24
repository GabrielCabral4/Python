nums = input('Insira 20 números: ').split()

for num in range(len(nums)):
	nums[num] = int(nums[num])

pares = []
impares = []

for a in range(len(nums)):
	if nums[a] % 2 == 0:
		pares.append(nums[a])

	else:
		impares.append(nums[a])
print(f'O vetor com os seus 20 números é esse: {nums}')
print(f'O vetor par desses números é: {pares}')
print(f'O vetor ímpar desses números é: {impares}')
