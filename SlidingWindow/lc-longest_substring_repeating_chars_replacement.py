"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""


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
            most_common_occurs = max(countChars.values())
            return True if (size - most_common_occurs <= k) else False
        
        res = 0
		
        for i in range(len(s)):            
            countCharsWindow = {}
			
            for j in range(i, len(s)):
                countCharsWindow[s[j]] = 1 + countCharsWindow.get(s[j], 0)
				
                if not _is_valid_window(countCharsWindow, j - i + 1, k):
                    j -= 1
                    break
            
            res = max(res, j - i + 1)


        return res


