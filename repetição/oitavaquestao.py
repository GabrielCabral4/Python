nums = input('Insira 5 números: ').split()

for i in range(len(nums)):
	nums[i] = int(nums[i])

soma = sum(nums)
print(f'A soma dos números é: {soma}')

media = soma / 5
print(f'A média dos números é: {media}')

