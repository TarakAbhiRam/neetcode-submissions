class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top , bottom = 0 , len(matrix)-1
        row = -1

        while top <= bottom:
            m = top + (bottom-top)//2

            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif target  < matrix[m][0]:
                bottom = m - 1
            else:
                top = m + 1
            
        if row == -1:
            return False
        
        l ,  r = 0 , len(matrix[row])-1
        while l <= r :
            mid = l  + (r-l)
            if matrix[row][mid] == target :
                return True
            elif matrix[row][mid]  < target :
                l = mid + 1
            else:
                r = mid - 1
        return False



        
        

        
                



            
