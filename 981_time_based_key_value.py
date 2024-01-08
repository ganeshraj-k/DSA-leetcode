from typing import List




class TimeMap:
	def __init__(self):

		self.dict1  = {}




	def sample_binary_search(self, list1, target):
		if not list1  or (len(list1)==1 and max(list1) > target) :
			return "NA"

		if max(list1) <= target:
			return len(list1)-1
		else:

			low = 0
			high = len(list1)-1
			while(low < high):
				mid = (low+high)//2
				
				if target >= list1[mid] and target <list1[mid+1]:
					
					return mid

				elif target > list1[mid+1]:
					
					low = mid
				elif target < list1[mid]:
					high = mid
		
		return mid
        



	def set(self, key: str, value: str, timestamp: int) -> None:
	    if key not in self.dict1:
	        val = []
	        ts = []
	        val.append(value)
	        ts.append(timestamp)
	        list_data = [val, ts]
	        self.dict1[key] = list_data
	    else:
	        list_data = self.dict1[key]
	        list_data[0].append(value)
	        list_data[1].append(timestamp)
	        self.dict1[key] = list_data


        
        

	def get(self, key: str, timestamp: int) -> str:

		if key not in self.dict1:
			print("not there")
			return ""

		list_ts = self.dict1[key][1]
		list_val = self.dict1[key][0]

		finder = self.sample_binary_search(list_ts, timestamp)
		
		if finder == "NA":
			
			return ""
		else:
			return list_val[finder]





		


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)      #// store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))         #// return "bar"
timeMap.get("foo", 3)     #// return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4) #// store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))         #// return "bar2"
timeMap.get("foo", 5);         #// return "bar2"     



