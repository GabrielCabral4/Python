nums = input('Insira uma lista com 10 números reais: ').split()

for i in range(len(nums)):
	nums[i] = float(nums[i])

nums.reverse()

print(nums)
