"""
Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Use binary search to find the first negative element of each row, 
            and as elements are sorted, 
        all elements after the first negative element will also be negative.

        Time: O(m logn), for each row, do binary search O(logn)
        Space: O(1)
        """

        countNegatives = 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        # Iterate on all rows of the matrix one by one.
        for row in grid:

            # Using binary search find the index
            # which has the first negative element.
            l, r = 0, num_cols - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] < 0:
                    r = mid - 1
                elif row[mid] >= 0:
                    l = mid + 1
            
            # 'left' points to the first negative element,
            # which means 'num_cols - left' is the number of all negative elements.
            countNegatives += (num_cols - l)

        return countNegatives


