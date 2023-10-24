nums = input('Insira 10 números inteiros: ').split()

pares = []
impares = []

for i in range(len(nums)):
	if int(nums[i]) % 2 == 0:
		pares.append(nums[i])

	else:
		impares.append(nums[i])

print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')
