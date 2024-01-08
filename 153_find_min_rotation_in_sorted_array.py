from typing import List

class Solution:
	def findMin(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]
		elif len(nums) == 2:
			return min(nums)


		low = 0
		high = len(nums) - 1
		min_ind = 0

		while( low < high):
			mid = (low+high)//2
			if nums[high] <= nums[mid]:
				min_ind = high
				low = mid+1
				high = high
			else:
				high = mid
				low = low
				min_ind = low

		return nums[min_ind]



sol = Solution()

print(sol.findMin( [3,1,2]))
