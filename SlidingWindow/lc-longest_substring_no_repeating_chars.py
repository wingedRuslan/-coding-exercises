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
        
        My first implementation of the sliding window. 
        I maintain set (unique chars in currest sliding window substring) and sliding window to track chars in substring.
        
        Time - O(n)
        Space -O(n)
        """
        
        MaxLenSubstring = 0
		
        charSet = set()
        slide_window_substring = ''

        for i in range(len(s)):
            
            # Repetition found
            if s[i] in charSet:
                
                # What is the current len of substring
                MaxLenSubstring = max(MaxLenSubstring, len(charSet))
				
                # Substring is continuous - so I need to know how many elements from left I need to remove
                # j = 0, s[i] repetition found for the 1st element in window
                # j > 0, s[i] - remove all elements to the left of repetition bc the substring must be continuous
                j = 0
                while slide_window_substring[j] != s[i]:
                    j += 1
                
                # Remove from hashset
                for c in slide_window_substring[ : j + 1]:
                    charSet.remove(c)

                # Remove from sliding window the left part before repetition seen
                slide_window_substring = slide_window_substring[j + 1 : ]


            charSet.add(s[i])
            slide_window_substring += s[i]
        
        # Edge case - " "
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

