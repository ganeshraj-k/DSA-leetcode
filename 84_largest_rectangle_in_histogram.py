
from typing import List
import json

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		maxarea = 0
		stack1 = []
		start = 0
		for i, height in enumerate(heights):
			start = i
			while stack1 and stack1[-1][1] > height:
				index, h = stack1.pop()
				print(stack1)
				maxarea = max(maxarea, h* ( i-index))
				start = index
		
			stack1.append([start , height])
			

		for i, el  in enumerate(stack1):
			maxarea = max(maxarea,  el[1]* (len(heights) - el[0]) )

		return maxarea



sol = Solution()
file = open("input_file.txt")
cont = json.load(file)

print(sol.largestRectangleArea(cont))



			


