import re

class Solution:
	def isPalindrome(self , s: str) -> bool:
		if s == " " or s == "" or len(s) == 1:
			return True

		s = re.sub(r'\W+', '', s)
		s = re.sub( "_",'',s )
		s = ''.join(s.split(' '))
		s = s.lower()
		print(s)
		for i in range( 0 , int((len(s)+1)/2)  ):
			if (s[i]) != s[len(s) - i - 1]:
				return False

		return True

















import json
fr = open("input_file.txt")
info = json.load(fr)
fr.close()

Sol = Solution()
print(Sol.isPalindrome(info))

