from typing import List

class Solution:
	def twoSum(self, nums: List[int] , target: int) -> List[int]:
		d1 = {}
		for i in range(0, len(nums)):
			if ((target - nums[i]) in d1 ):
				return [i, d1[target - nums[i]]]
			d1[nums[i]] = i
		return []








target, nums = input("enter a list and a target").split(" ")
target = int(target)
nums = nums.split(',')
nums = [int(i) for i in nums]
print(target , nums)
sol = Solution()
print(sol.twoSum(nums, target)  )	
