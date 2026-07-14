class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[row])-1

        while col >= 0 and (len(matrix))> row >= 0:
            print(row, col)
            if matrix[row][col] < target:
                row += 1
                continue
            if matrix[row][col] > target:
                col -= 1
                continue
            if matrix[row][col] == target:
                return True
        return False


        
        