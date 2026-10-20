class Solution:
    def isValid(self, arr):
        nums = set(map(str, range(1, 10)))
        for num in arr:
            if num == "." or num in nums:
                nums.discard(num)
                continue
            return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal
        for row in board:
            if not self.isValid(row):
                return False
        
        # Check vertial
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not self.isValid(col):
                return False
        
        # check block
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                block = [board[p][q] for p in range(i, i+3) for q in range(j, j+3)]
                if not self.isValid(block):
                    return False
                j += 3
            i += 3
        return True