"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""


class SortingSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        For interval problems - draw the number line to understand the problem and come up with a solution.

        - sort input list of intervals
        - overlapping intervals will form contiguous blocks. 

        If we sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

        Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O()nlogn) complexity of sorting.
                
        Time - O(nlogn)
        Space - O(logn) - the sorting itself takes O(log⁡n) space
        """
        
        output = list()

        # Sort input list of intervals
        intervals.sort(key=lambda x: x[0])
        
        for interval in intervals:
            
            # if the list of merged intervals is empty
            if not output:
                output.append(interval)
            
            lastEnd = output[-1][1]                         # the end of the last element in output

            if interval[0] <= lastEnd:                      # overlap, so we merge the current and previous intervals
                output[-1][1] = max(lastEnd, interval[1])   # edge case, e.g. [1, 5], [2, 4]
            else:
                output.append(interval)                     # no overlap - simply append current interval to output
        
        return output


