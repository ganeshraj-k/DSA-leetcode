
from typing import List

class Solution:
	def maxProfit(self, prices: List[int] ) -> int:

		maxprof = 0
		minprice = prices[0]


		for price in prices:
			maxprof = max(   maxprof , price - minprice)
			minprice = min( minprice , price)
		
		
		return maxprof



sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4]))






