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
        This is the 3rd iteration over my Sliding Window Solution.

        Given a substring with a fixed end index in the string
            maintain a set to record each unique character in the current substring 
            if any character occurs more than once (repetition), drop the leftmost characters until there are no duplicate characters.

        Time - O(n)
        Space - O(n)
        """

        MaxLenSubstring = 0

        # Keep unique chars of the sliding window
        charSet = set()
        
        # Points to the start of the substring
        start_substring_pointer = 0

        for i in range(len(s)):
            
            # Repetition found - Update window and set
            while s[i] in charSet:
                charSet.remove(s[start_substring_pointer])
                start_substring_pointer += 1
            
            # Increase the "end" of current substring by one - consider next element
            charSet.add(s[i])

            # Keep track of the longest substring without repeating characters
            MaxLenSubstring = max(MaxLenSubstring, i - start_substring_pointer + 1)
        
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

