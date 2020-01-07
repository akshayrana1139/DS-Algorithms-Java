from typing import List
class Solution:
# Runtime: 92 ms, faster than 88.98% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Sudoku.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_r = set()
        set_c = set()
        set_b = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        a = board
        for i in range(9):
            for j in range(9):
                if a[i][j] != ".":
                    if a[i][j] in set_r:
                        return False
                    if a[i][j] not in set_r: # rows
                        set_r.add(a[i][j])
                if a[j][i] != ".":
                    if a[j][i] in set_c:
                        return False
                    if a[j][i] not in set_c: # columns
                        set_c.add(a[j][i])
                    
                index = 3*int(i/3)+int(j/3)
                if a[i][j] != ".":
                    if a[i][j] in set_b[index]:
                        return False
                    if a[i][j] not in set_b[index]:
                        set_b[index].add(a[i][j])
            set_r = set()
            set_c = set()
        return True

if __name__ == "__main__":
    a = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    print(Solution().isValidSudoku(a))
        
                    
                    
                    
            