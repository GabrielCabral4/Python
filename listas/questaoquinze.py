from statistics import mean
contador = 0
nums = []

while True:
	num = int(input('Insira um número: '))
	if num < 0: break
	contador += 1
	nums.append(num)

print(contador)
for i in range(len(nums)):
	print(nums[i], end = ' ')
for j in range(len(nums)):
	reverso = nums.reverse()
	print(reverso)
	break
soma = sum(nums)
print(soma)
media = mean(nums)
print(media)
acima_media = 0
for a in range(len(nums)):
	if nums[a] > media:
		acima_media += 1
print(acima_media)
abaixo_7 = 0
for b in range(len(nums)):
	if nums[b] < 7:
		abaixo_7 += 1
print(abaixo_7)
print('fim')
