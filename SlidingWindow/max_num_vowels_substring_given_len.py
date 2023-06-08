"""
Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Typical sliding window approach:
        - "substring (subarray) of length k" equivalent to "window of length k"

        But problem: 
            - if we count the number of vowels in each window by iteration every time, 
                it would result in a time complexity of O(length_of_s⋅k) - expensive. 
        
        Solve:
            - two adjacent windows only differ by two characters
            - move the index of the right boundary of the window from i - 1 to i, 
                only one char is added to the window while one is removed    
        --> represent the new window by keeping track of the changes between adjacent windows

        Time: O(n)
        Space: O(1)
        """

        vowels = {'a', 'e', 'i', 'o', 'u'}

        maxVowels = 0

        # Build the window of size k, 
        # count the number of vowels it contains.
        numVowels = 0
        for char in s[:k]:
            if char in vowels:
                numVowels += 1
        maxVowels = numVowels

        # windows defined by start and end
        start = 0
        for end in range(k, len(s)):

            if s[end] in vowels:
                numVowels += 1
            
            if s[start] in vowels:
                numVowels -= 1
            
            maxVowels = max(maxVowels, numVowels)
            
            start += 1
        
        return maxVowels


"""
        ### Time - O(len(s) * k)
        maxVowels = 0

        # windows defined by start and end
        start = 0
        for end in range(k, len(s)):

            # calc num. vowels in windows
            numVowels = 0
            for char in s[start:end]:
                if char in ['a', 'e', 'i', 'o', 'u']:
                    numVowels += 1

            maxVowels = max(maxVowels, numVowels)
            
            start += 1
        
        return maxVowels
"""

