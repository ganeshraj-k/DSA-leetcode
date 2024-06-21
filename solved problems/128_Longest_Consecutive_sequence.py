from typing import List

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return 0
		nums_set = set(nums)

		max_count = 0

		for i in nums_set:
			counter = 1
			curr = i 
			if ( i-1 not in nums_set):
				while(curr+1 in nums_set):
					counter = counter + 1
					curr = curr + 1
			max_count = max(max_count, counter)

		return max_count













import json


fr  = open("input_file.txt")
lst  = json.load(fr)
Sol = Solution()
print(Sol.longestConsecutive(lst))
fr.close()