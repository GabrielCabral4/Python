vetores = input('Insira 10 números inteiros para o vetor: ').split()

soma = 0
for vetor in range(len(vetores)):
	soma += int(vetores[vetor]) ** 2

print(f'A soma dos quadrados dos números desse vetor resulta em: {soma}')
