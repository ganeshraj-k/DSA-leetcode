from typing import List

class Solution:
	def searchMatrix(self, matrix: List[List[int]] , target: int) -> bool:

		rows = len(matrix)
		cols = len(matrix[0])

		if rows == cols and rows == 1:
			return matrix[0][0] == target


		n_of_items = rows * cols

		low = 0
		high  = n_of_items - 1

		while(low <= high):
			mid = int((low+high)/2)
			r, c = self.get_2ditem(mid, cols, matrix)
			item = matrix[r][c]
			if target == item:
				return True
			elif target < item:
				low = low
				high = mid-1
			else:
				low = mid + 1
				high = high


		return False




	
	def get_2ditem( self, index,  cols , matrix):

			return  int(index/cols)  ,  index%cols




import json

file = open("input_file.txt")

cont = json.load(file)

sol = Solution()
print(sol.searchMatrix(cont, 3))