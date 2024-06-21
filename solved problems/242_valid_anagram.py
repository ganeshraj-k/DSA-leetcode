# valid anagram https://leetcode.com/problems/valid-anagram/


# use dictionary instead of list


from collections import Counter
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
	    if len(s) != len(t):
	    	return False
	    d1 = {}

	    for i, j in zip(s,t):
	    	if i in d1:
	    		d1[i] = d1[i] + 1
	    	else:
	    		d1[i] = 1

	    	if j in d1:
	    		d1[j] = d1[j] - 1
	    	else:
	    		d1[j] = -1
	    print(d1)
	    return not any(d1.values())





	    # for i,j in zip(s,t):
	    	
	    # return count == [0]*26







s,t = input("enter two strings").split(" ")
print(s)
print(t)
sol  = Solution()
print(sol.isAnagram( s, t))
s_count  = Counter(s)
print(len(s_count))

	