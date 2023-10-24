nums = input('Insira 5 números: ').split()

for a in range(len(nums)):
	nums[a] = int(nums[a])

maior_num = nums[0]

for i in range(len(nums) - 1):
	if nums[i] > maior_num:
		maior_num = nums[i]


print(maior_num)
