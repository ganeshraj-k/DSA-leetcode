
class Solution:
	def  lengthOfLongestSubstring( self, s: str) -> int:
		if s == "":
			return 0

		strmax = s[0]
		str2 =""

		for i in s:
			

			
			if i not in str2:
				str2+= i
				
				
			else:


				str2 = str2[str2.find(i)+1 : ] + i
			
			
			if len(str2) > len(strmax):
				strmax = str2



		return len(strmax)



sol = Solution()

print(sol.lengthOfLongestSubstring( "dvdf"))




