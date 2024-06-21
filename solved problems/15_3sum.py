from typing import List


class Solution:

	def threeSum(self, nums: List[int]) -> List[List[int]]:
		out_list = []
		nums.sort()
		for i in range(0, (len(nums)-2) ):
			if (i >0 and nums[i] == nums[i-1]):
				continue

			low   = i + 1
			high  = len(nums) - 1

			while(low < high):
				if( nums[low]  + nums[high]  == (0 - nums[i])) :
					out_list.append([ nums[i] , nums[low] , nums[high]])
					print(low)
					while(low < high and  nums[low] == nums[low+1] ):
						low = low+1
						
					while(low < high and nums [high] == nums[high-1]):
						high = high-1
					low+=1
					high-=1
				elif(nums[low] + nums[high]  < (0-nums[i])):
					low+=1
				else:
					high-=1
		return out_list


				












import json


sol = Solution()


fr = open("input_file.txt")
input_list = json.load(fr)
input_list.sort()
print(input_list)

print(sol.threeSum(input_list))



		