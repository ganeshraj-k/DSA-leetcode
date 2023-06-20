from typing import List

class Solution:
	def productExceptSelf(self, nums: List[int] ) -> List[int] :
		result = [1] * len(nums)

		for i in range(1, len(nums)):
			result[i] = result[i-1] * nums[i-1]

		suff_prod = nums[len(nums)-1]
		for i in range(len(nums)-2, -1, -1):
			
			result[i] = suff_prod * result[i]
			suff_prod = suff_prod * nums[i]
			

		return result







	# def productExceptSelf(self, nums: List[int]) -> List[int] :
	# 	prod = 1
	# 	for i in nums:
	# 		prod = prod * i
	# 	out_list = []


	# 	for i in range(0, len(nums)) :
	# 		if nums[i] == 0:
	# 			out_list.append(self.prod_except_one(nums, i))
	# 			continue
	# 		out_list.append(int(prod/nums[i]))
	# 	return out_list

	# def prod_except_one(self, nums: List[int], num: int):
	# 	prod = 1
	# 	for i in range(0, len(nums)):
	# 		if i == num:
	# 			continue
	# 		prod = prod*nums[i]

	# 	return prod








nums = input("enter an array").split(',')
nums = [int(i) for i in nums]
sol = Solution()
print(sol.productExceptSelf(nums))

