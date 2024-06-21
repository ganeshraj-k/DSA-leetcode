#https://leetcode.com/problems/group-anagrams/description/

from typing import List



class Solution:
	def groupAnagram(self, strs: List[str]) -> List[List[str]]:
		d_s = {}
		for s  in strs:
			
			if ''.join(sorted(s)) in d_s:
				d_s[''.join(sorted(s))].append(s)
			else:
				d_s[''.join(sorted(s))] = [s]
		return d_s.values()











strs = input("enter strings").split(' ')
print(strs)
sol = Solution()
print(sol.groupAnagram(strs))
