'''
Set Matrix Zeroes
Leetcode : https://leetcode.com/problems/set-matrix-zeroes/

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

'''

from typing import List 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        

if __name__ == "__main__":
    sl = Solution()
    mat = [[0 for i in range(3)] for j in range(4)]
    sl.setZeroes(mat)