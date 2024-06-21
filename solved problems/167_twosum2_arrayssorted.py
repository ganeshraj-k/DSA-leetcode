
from typing import List

class Solution:
	


	def twoSum(self, nums: List[int] , target: int)  -> List[int] :
		a_pointer = 0
		b_pointer = len(nums) - 1

		while( a_pointer < b_pointer):

			if (nums[a_pointer]  + nums[b_pointer]   < target) : 
				a_pointer+=1
			elif ( nums[a_pointer]  + nums[b_pointer]   > target ):
				b_pointer-=1
			else :
				return [a_pointer+1, b_pointer+1]
		return [a_pointer+1, b_pointer+1]







		# brute force method
		# for i in range(0, len(nums)):
		# 	if (target - nums[i]) in nums[i + 1: ]:
		# 		return [i +1 , i+1 + (nums[i+1 : ].index(target - nums[i]))+1]




















fr = open("input_file.txt")
read_input = fr.readlines()
read_input1 = read_input[0]

read_input1 = read_input1.split(' ')
fr.close()

list1 = eval(read_input1[2])
target = eval(read_input1[5])
print(list1, target)

Sol = Solution()
print(Sol.twoSum( list1, target))
