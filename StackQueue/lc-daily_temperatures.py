"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""


class StackSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        To aim for O(n), do not look at the right part after i, BUT at the left part at position i --> remember the previous elements.
        How? --> add seen temperatures to stack. At position i, lookup the temp at (i-1), (i-2) etc. and check > < currTemp to previous.
        
        While iterating over {temperatures}, we have to remember the previous temps (and their index) we looked at.
        Use stack to remember previous temps and index!

        [73, 74, 75 ...] --> when at (74), pop from stack (73), assign 1
        [73, 72, 71 ...] --> keep adding to the stack --> stack will have monotonically decreasing order
        [73, 72, 75 ...] --> at (75) j, if the last element (at i) in stack < 75, assign (j - i). pop the last element - remove since it was assigned. Repeat for the rest elements in stack while (75) > stack.top()
        
        These rules make stack in non-increasing order
        
        Time - O(n)
        Space - O(n)
        """
        
        answer = [None] * len(temperatures)
		
        # Keep pairs (temperature, index)
        stack = []
		
        for i in range(len(temperatures)):
        	    
            # if currTemp > stack.top(), update answer && remove from stack element that was assigned
            while stack and temperatures[i] > stack[-1][0]:
                lower_temp, pos = stack.pop()
                answer[pos] = (i - pos)
            
            # add to the stack if currTemp < stack.top() and the currTemp
            stack.append((temperatures[i], i))
		
        # assign 0 to the remaining elements in stack
        while stack:
            temp, pos = stack.pop()
            answer[pos] = 0
        
        return answer


class BruteForceSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Straightforward solution - for each day, find the next day when temp > temp_at_curr_day
		
        Time - O(n**2)
        Space - O(1)
        """
		
        answer = [None] * len(temperatures)
		
        for i in range(len(temperatures) - 1):
            currTemp = temperatures[i]
            
            is_found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > currTemp:    # found day when temp > currTemp
                    answer[i] = (j - i)
                    is_found = True
                    break
			
            if not is_found: answer[i] = 0
		
        # the last day always 0
        answer[-1] = 0
        
        return answer

