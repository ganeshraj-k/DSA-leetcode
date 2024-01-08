from typing import List
from math import ceil


class Solution:
	def minEatingSpeed(self, piles: List[int] ,  h : int) -> int:
		
		right = max(piles)
		left = 0

		while(left+1 < right):
			mid  = (left+right)//2
			
			if self.caneat(piles, h , mid):

				right = mid

			else:
				left = mid

		return right





		

	def caneat(self, piles, h, k):
		h_total = 0
		for pile in piles:
			h_total  += ceil(pile/k)
		return h_total <= h



sol = Solution()

print(sol.minEatingSpeed([3, 6, 7, 11] , 8))
