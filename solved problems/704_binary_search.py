from typing import List
import json

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0  or (len(nums) == 1 and nums[0] != target):
            return -1
        elif (len(nums) == 1 and nums[0] == target):
            return 0



        lower = 0
        higher = len(nums) - 1
        

        while(lower <= higher):
            mid = (lower+higher)//2
            print(mid)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lower = mid+1

            else:
                higher = mid-1
        return -1

sol = Solution()
file = open("input_file.txt")
cont = json.load(file)
print(sol.search( [1,3], 3))




        