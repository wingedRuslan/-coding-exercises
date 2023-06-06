"""
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        """
        Min meetings room ~ What is the maximum number of overlapping meetings at any given point in time?

        Draw a picture to come up with a solution!

        Split the start and end times in two separate sorted arrays with only starts and ends.
        Use Two Pointer Technique to either move start pointer or end pointer.
        	- Move start pointer if a new meeting has to be places, meaning start[s] < end[e]
        	- Move end pointer if a meeting needs to be closed, meaning start[s] >= end[e] 
		
        Time -  O(nlogn)
        Space - O(n)
        """
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # res - the max(count) at a given point, count - overlapping meetings at a certain point
        res, count = 0, 0

        # Two pointers, s points at start, e points at end
        s, e = 0, 0
        
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res


