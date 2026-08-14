class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # Handle empty matrix or empty rows
            return False
    
        ls = len(matrix)
        s, l = 0, ls - 1
        
        # Binary search to find the row
        while s <= l:
            mid = (s + l) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][-1] == target:
                return True
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break  # Target might be in this row
            elif matrix[mid][0] > target:
                l = mid - 1
            else:
                s = mid + 1
        
        # If no valid row is found
        if s > l:
            return False
        
        # Binary search within the row
        row = mid
        s, l = 0, len(matrix[row]) - 1
        while s <= l:
            m = (s + l) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                l = m - 1
            else:
                s = m + 1
        
        return False