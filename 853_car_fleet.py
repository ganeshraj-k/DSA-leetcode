from typing import List


class Solution:
	def carFleet(self, target: List[int] , position: List[int], speed: List[int]) -> int: 
		if len(speed) == 1:
			return 1
		

		fleet = []
		pairs = sorted([ [i,j]  for i, j in zip(position, speed)])
	

		for pos, speed in pairs[: : -1]:

			time = (target - pos )/(speed)
			if not fleet:
				fleet.append( [pos, speed, time])
			elif fleet[-1][2] < time:
				fleet.append([pos, speed, time])

		return len(fleet)



sol = Solution()



import json
file = open("input_file.txt")
cont = json.load(file)  
print(sol.carFleet(cont[0] , cont[1] , cont[2]))

