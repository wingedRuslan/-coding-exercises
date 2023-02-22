"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest  substring  without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class SlidingWindowSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Uses a slide window method to narrow down the search range.
        
        Sliding window solution - next iteration. 
        I maintain set (unique chars in currest sliding window substring) and sliding window to track chars in substring.
        Sliding window is specified via 2 pointers: start (points to substring start) and curr pointer while iterating through string.
        	--> Makes code cleaner and easy-to-follow
        
        Time - O(n)
        Space -O(n)
        """
        
        MaxLenSubstring = 0

        # Keep unique chars of the sliding window
        charSet = set()
        
        # Points to the start of the substring
        start_substring_pointer = 0

        for i in range(len(s)):

            if s[i] in charSet:    # Repetition found - Update window and set
                
                # Remove chars before the repetition - remember that the substring contains continuous elements
                while s[start_substring_pointer] != s[i]:
                    charSet.remove(s[start_substring_pointer])
                    start_substring_pointer += 1
                
                # Remove the repetition element itself
                charSet.remove(s[i])
                start_substring_pointer += 1
            
            charSet.add(s[i])

            MaxLenSubstring = max(MaxLenSubstring, len(charSet))


        return MaxLenSubstring


class BruteForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Check every single substring, check whether it has duplicates, take the longest substring without repetition
        
        While iterating through each character:
            substring starts at the current character
            check when hit the repetition with the hashset
            len(hashset) = Longest Substring Without Repeating Characters
        
        Time - O(n**2)
        Space - O(n)
        """

        MaxLenSubstring = 0

        for ind, char in enumerate(s):
            
            SubstringChars = set()

            while ind < len(s) and s[ind] not in SubstringChars:
                SubstringChars.add(s[ind])
                ind += 1

            MaxLenSubstring = max(MaxLenSubstring, len(SubstringChars))

        return MaxLenSubstring

