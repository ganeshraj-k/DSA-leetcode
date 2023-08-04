from typing import List

class Solution:
	def trap(self, height: List[int]) -> int:
		trap = 0
		low = 1
		high = len(height)-2

		lmax = height[0]
		rmax = height[len(height)-1]

		while low <= high:
			if lmax <= rmax:
				trap = trap + max(0,   (lmax - height[low]))
				lmax = max(height[low] , lmax)
				low = low +1
			else:
				trap = trap + max(0,   (rmax - height[high]))
				rmax = max(height[high] , rmax)
				high = high -1
			print(trap)
		return trap






		# O(n) method ***************************************************************************************************
		# trap = 0

		# lmax = [height[0]]
		# rmax = [height[len(height)-1]]

		# for i in range(1, len(height)):
		# 	lmax.append(max(height[i-1] , lmax[i-1]))
		# 	rmax.append(max (height[len(height)-1-i] , rmax[i-1]))


		# for i in range(0, len(height)):
		# 	trap = trap + max(0, (min(lmax[i] , rmax[len(height)-1-i])  - height[i]  )     )

		# return trap






		# brute force method ******************************************************************************************
		# mh = max(height)
		# trap = 0
		# for j in range( 0, mh+1):
		# 	curr = 0
		# 	i = 1
		# 	while(i < len(height)-1):

		# 		if (height[i] == j  and height[i] < height[i-1]):
					
		# 			while(   height[i] <= j and i < len(height)-1):
						
						
		# 				curr+=1
		# 				i+=1
		# 			if( height[i] > height[i-1] ):
		# 				trap = trap + curr
						
		# 				curr = 0
		# 		i+=1

		# 	for k in range(0, len(height)):
		# 		if height[k] == j:
		# 			height[k] = j+1

		# return trap



















import json
fr = open("input_file.txt")
input_list = json.load(fr)
fr.close()

sol = Solution()
print(sol.trap(input_list))