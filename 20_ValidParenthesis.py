

class Solution:
	def isvalid(self, s: str) -> bool:

		stack1 = []
		brackets = {}
		brackets['{'] = '}'
		brackets['['] = ']'
		brackets['('] = ')'

		for i in s:

			
			if i in list(brackets.keys()):
				stack1.append(i)
			elif  (len(stack1) != 0 ) and  (brackets[stack1[len(stack1) - 1]] == i) :
				
				stack1.pop()
			else:

				
				return False

		return len(stack1) == 0




fr = open("input_file.txt")
read_input = fr.readlines()
read_input1 = read_input[0]

sol = Solution()
print(sol.isvalid(read_input1))

