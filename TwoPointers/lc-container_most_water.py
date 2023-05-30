"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two-pointer technique at [start] and [end].
            1. calculate current area 
            2. compare to maxArea
            3. move the smallest height to the next position (-> or <-)

        Time - O(n)
        Space - O(1)
        """

        start = 0
        end = len(height) - 1

        maxArea = 0

        while start < end:
            # current area
            common_height = min(height[start], height[end])
            curr_area = common_height * (end - start)
            maxArea = max(maxArea, curr_area)
            
            # move one of pointers - the smallest one
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        
        return maxArea


