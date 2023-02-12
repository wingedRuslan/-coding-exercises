"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Idea: row+col are the same for elements in one diagonal.
        1) Keep together elements that have the same pos(=row+col) as key in a hashmap
        2) Iterate over each {pos} in hashmap, if pos - even --> reverse the array, else just output [elements] at odd {pos}
        
        Time - 0(m*n)
        Space - 0(m*n)
        """
        
        # hashtable to store (row+cols) = matrix[row][col]
        diag_elements = defaultdict(list)
        
        # keep diagonal elements together - Fill-in the hashtable
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                diag_elements[row+col].append(mat[row][col])
        
        # keep final results
        output_arr = []
        
        for mat_pos in diag_elements: 
            # for every odd (row+col) reverse elements
            if (mat_pos % 2) == 0:
                diag_elements[mat_pos].reverse()
            
            output_arr = output_arr + diag_elements[mat_pos]
        
        return output_arr


