from typing import List

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return 0
		
		nums = set(nums)
		nums = list(nums)
		nums.sort()
		print(nums)

		counter = 1
		countmax = 1
		for i in range(1, len(nums)):
			print(counter, nums[i])
			if nums[i] == nums[i-1]+1:
				counter  = counter+1
			else:
				countmax  = max(countmax, counter)
				counter = 1
			countmax  = max(countmax, counter)

		return countmax







import json


fr  = open("input_file.txt")
lst  = json.load(fr)
Sol = Solution()
print(Sol.longestConsecutive(lst))
fr.close()