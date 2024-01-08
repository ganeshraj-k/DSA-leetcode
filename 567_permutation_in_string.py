

class Solution:
	def checkInclusion( self, s1: str, s2: str) -> bool:

		letcount = {}
		win = len(s1)

		if len(s1) > len(s2):
			return False


		for l in s1:
			if l in letcount:
				letcount[l] = letcount[l]+1
			else:
				letcount[l] = 1



		for i in range(0 , len(s2)):

			if s2[i] in letcount:
				dict_count = self.lettercounter(s2[i : i+win])
				if dict_count == letcount:
					return True

		return False






	def lettercounter(self, s: str)  -> dict :


		letcount = {}
		

		for l in s:
			if l in letcount:
				letcount[l] = letcount[l]+1
			else:
				letcount[l] = 1

		return letcount





sol = Solution()


print(sol.checkInclusion("ab" , "hahdggba"))