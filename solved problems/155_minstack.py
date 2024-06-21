

class MinStack:

	def __init__(self):
		self.stack1 = []
		self.min_val = 10^9


	def push(self ,  val: int) :
		if not self.stack1:
			self.stack1.append(val)
			self.min_val = val

		else:
			if( val < self.min_val):
				self.stack1.append(  2*val   - self.min_val)
				self.min_val = val
			else:
				self.stack1.append(val)
	def pop(self):
		if not self.stack1:
			return
		tp = self.stack1[len(self.stack1)-1]
		self.stack1.pop()
		if(tp  < self.min_val):
			self.min_val = 2* self.min_val - tp




	def top(self)  -> int:
		if not self.stack1:
			return


		tp =  self.stack1[len(self.stack1)-1]
		if(tp  < self.min_val):
			tp = self.min_val
		return tp


	def getMin(self) -> int:
		if not self.stack1:
			return
		return self.min_val






	# def push(self, val: int) :
	# 	if ( len(self.mins) == 0 or val < self.mins[0]):
	# 		self.mins.append(val)
	# 	self.stack1.append(val)
	# 	return None


	# def pop(self ) :
	# 	if self.top() == self.getMin():
	# 		self.mins.pop()


	# 	self.stack1.pop()
	# 	return None

	# def top(self)  -> int:
	# 	if len(self.stack1) == 0:
	# 		return None


	# 	return self.stack1[len(self.stack1)-1]

	# def getMin(self) -> int:
	# 	if len(self.mins) == 0:
	# 		return None
	# 	return self.mins[len(self.mins) - 1]







stack2  = MinStack()
stack2.push(0)
stack2.push(1)
stack2.push(0)

print(stack2.getMin())
stack2.pop()

print(stack2.getMin())
