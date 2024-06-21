

from typing import List
import json


class Solution:
	def search(self, nums: List[int] , target: int) -> int:

		if len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
			return -1
		if len(nums) == 0 and Nums[0] == target:
			return 0

		low = 0 
		high = len(nums) - 1

		while(low < high):
			mid = (low + high)//2

			if nums[high] <= nums[mid]:
				min_ind = high
				low = mid+1
			else:
				min_ind = low
				high = mid

		
		
		length = len(nums)

		low = 0
		high = length-1



		while(  low <= high):

			
			
			mid = (low+high)//2
			
			mid_curr = self.curr_pos(length, min_ind , mid)
			
			if nums[mid_curr] == target:
				return mid_curr
			elif target > nums[mid_curr]:
				low = mid+1
			else:
				high = mid-1


		return -1





	def curr_pos( self, length: int, offset: int, pos: int) -> int:

		return (  pos + offset)%length










fileread = open("input_file.txt")
sol = Solution()
print(sol.search(  [1,3]  , 3))

