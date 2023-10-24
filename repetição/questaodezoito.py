nums = input('Insira alguns números para formar um vetor: ').split()

for i in range(len(nums)):
	nums[i] = int(nums[i])

maior = max(nums)
menor = min(nums)
soma = sum(nums)

print(f'O maior número desse vetor é: {maior}')
print(f'O menor número desse vetor é: {menor}')
print(f'A soma dos números desse vetor é: {soma}')
