"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""


class SlidingWindowSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding Window solution (two pointers) as an upgrade over BruteForceSolution
        
        How to check is_valid_window?
			- window_length - most_common_el_occurrences <= k

        Init l, r at the 1st position
        if current windows s[l:r] is valid 
            --> move r to the right
        if current windows s[l:r] is NOT valid 
            --> move l to the right until valid window is found
            --> remove elements from the hashmap as we shrink the window (l += 1, r-const)

        Note: _is_valid_window() is technically constant in time complexity because contains at most 26 uppercase English letters

        Time - O(26*n)
        Space - O(n)
        """
        
        # def _is_valid_window(countChars, size, k):
        #     # Rule to check whether the current windows is valid or not
        #     maxFreq = max(countChars.values())
        #     return True if (size - maxFreq <= k) else False
        
        res = 0

        # Keep the char counts of the current window
        count = {}

        l = 0
        r = 0

        while r < len(s):
            
            count[s[r]] = 1 + count.get(s[r], 0)

            # Shrink the window (move left pointer) until valid window found
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

            # Extend the window
            r += 1

        return res


class BruteForceSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Check every single substring if it is valid or not.
        Iterate over every char in s, if current window (substring) is valid, increment window + 1, repeat.
        
		how to check is_valid_window?
			- window_length - most_common_el_occurrences <= k
		
        how to get most_common_el_occurrences in a current window?
        	- Hashmap
        
        Working solution but not optimal and hits TLE error.
        
        Time - O(n**2)
        Space - O(n)
        """
        
        def _is_valid_window(countChars, size, k):
            # Rule to check whether the current windows is valid or not
            maxFreq = max(countChars.values())
            return True if (size - maxFreq <= k) else False
        
        res = 0
		
        for i in range(len(s)):            
            countCharsWindow = {}
			
            for j in range(i, len(s)):
                countCharsWindow[s[j]] = 1 + countCharsWindow.get(s[j], 0)
				
                if not _is_valid_window(countCharsWindow, j - i + 1, k):
                    j -= 1    # return to the previous valid window
                    break
            
            res = max(res, j - i + 1)


        return res


