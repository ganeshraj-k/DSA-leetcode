from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        dict1 = {}
        for i in range(1,10):
            dict1[i] = 0   








        for l in board:
            dict2 = dict1.copy()
            
            for i in l:
                if i == '.':
                    continue
                dict2[int(i)] = dict2[int(i)] + 1
                if dict2[int(i)] > 1:
                    print(dict2[int(i)])
                    return False

        for i in range(0,9):
            dict2 = dict1.copy()
            for j in range(0,9):
                
                if board[j][i] == '.':
                    continue

                dict2[int(board[j][i])]  = dict2[int(board[j][i])] + 1
                if dict2[int(board[j][i])] > 1:
                    
                    return False

        for k in range(0,9,3):
            for l in range(0, 9, 3):
                    dict2 = dict1.copy()
                    for i in range(k, k+3):
                        for j in range(l, l+3):
                            if board[j][i] == '.':
                                    continue

                            dict2[int(board[j][i])]  = dict2[int(board[j][i])] + 1
                            if dict2[int(board[j][i])] > 1:
                    
                                    return False





        return True























import json





fr  = open("input_file.txt")



lst  = json.load(fr)






Sol = Solution()
print(Sol.isValidSudoku(lst))


fr.close()