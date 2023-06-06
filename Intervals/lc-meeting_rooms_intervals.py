"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflic
"""

from typing import (
    List,
)


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        """
        Most intuitive solution is the most suitable, BUT
            !intervals has to be sorted! 
        
        The start of the next meeting must be after the end of the previous meeting.

        Time - O(nlogn)
        Space - O(logn)
        """

        # Sort meetings by the start time
        intervals.sort(key = lambda x: x.start)
		
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        
        return True


