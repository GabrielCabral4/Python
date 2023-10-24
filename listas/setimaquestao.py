vetor = input('Insira um vetor com cinco números inteiros: ').split()

for num in range(len(vetor)):
	vetor[num] = int(vetor[num])

soma = sum(vetor)
print(f'A soma desses cinco números é: {soma}')

multiplicação = vetor[0]
for i in range(1, len(vetor)):
	multiplicação *= vetor[i]

print(f'A multiplicação dos números desse vetor é: {multiplicação}')
