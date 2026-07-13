class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isUniqueArr(row):
                return False

        for c in range(9):
            col = [board[r][c] for r in range(9)]
            if not self.isUniqueArr(col):
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                grid = [
                    board[i][j]
                    for i in range(r, r + 3)
                    for j in range(c, c + 3)
                ]
                if not self.isUniqueArr(grid):
                    return False

        return True

    def isUniqueArr(self, arr: List[str]) -> bool:
        nums = [x for x in arr if x != "."]
        return len(nums) == len(set(nums))