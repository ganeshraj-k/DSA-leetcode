

# question https://leetcode.com/problems/contains-duplicate/description/

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for i in nums:
            if i in set1:
                return True
            else:
                set1.add(i)
        return False
        







list1 = input("enter a list").split()
sol = Solution()
print(sol.containsDuplicate(list1))

