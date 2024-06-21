from collections import Counter
from typing import List
import heapq

class Solution:
	def topKFrequent(self, nums: List[int] , k: int) -> List[int]:
		count = Counter(nums)
		return heapq.nlargest(k, count.keys(), key=count.get)








k,nums = input("enter a number and a list of numbers").split(' ')
k = int(k)
nums = nums.split(',')
nums = [int(i) for i in nums]
print(k , nums)
sol = Solution()
print(sol.topKFrequent(nums, k))
