from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()
        for i in range(0,9):
            for j in range(0,9):
                
                if board[i][j] != "." :
                    x1 = str(board[i][j]) + " in row" +str(i)
                    x2 = str(board[i][j]) + " in col" +str(j)
                    x3 = str(board[i][j]) + " in box" +str(int(i/3)) + " and " + str(int(j/3))
                else:
                    continue

                

                if x1 not in seen and x2 not in seen and  x3 not in seen: 
                    seen.add(x1)
                    seen.add(x2)
                    seen.add(x3)
                else:
                    
                    return False
        return True



import json



fr  = open("input_file.txt")
lst  = json.load(fr)
Sol = Solution()
print(Sol.isValidSudoku(lst))
fr.close()