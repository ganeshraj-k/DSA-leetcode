from typing import List

class Solution:
	def dailyTemperatures (self, temperatures : List[int])	-> List[int]:

		stack = []
		res = [0] * len(temperatures)


		for i in range ( 0, len(temperatures)) :

			if not stack    or  (stack[len(stack)  - 1][1]   >=   temperatures[i]):
				stack.append( [i , temperatures[i]])
			else:
				if(  stack[len(stack)  - 1][1]   <    temperatures[i]) :
					while (  stack[len(stack)  - 1][1]   <    temperatures[i]):

						res[ stack[len(stack)  - 1][0] ] = (i - stack[len(stack)  - 1][0]  )
						stack.pop()
						if(len(stack) == 0):
							break
					stack.append( [i , temperatures[i]])

		return res


			

sol = Solution()

print( sol.dailyTemperatures([73,74,75,71,69,72,76,73]) )






