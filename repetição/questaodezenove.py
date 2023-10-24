nums = input('Insira números entre 0 e 1000 para formarem um vetor: ').split()
for i in range(len(nums)):
	nums[i] = int(nums[i])

negativo = 0
maior_1000 = 0

for j in range(len(nums)):
	if nums[j] < 0:
		negativo += 1
	if nums[j] > 1000:
		maior_1000 += 1

if negativo != 0:
	print(f'O vetor inserido não se encaixa no intervalo pedido na questão pois um de seus números é negativo.')

elif  maior_1000 != 0:
	print(f'O vetor inserido não se encaixa no intervalo pedido na questão pois um de seus números é maior do que 1000.')

else:
	maior = max(nums)
	menor = min(nums)
	soma = sum(nums)
	print(f'O maior número desse vetor é: {maior}')
	print(f'O menor número desse vetor é: {menor}')
	print(f'A soma dos números desse vetor é: {soma}')
