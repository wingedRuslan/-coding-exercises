'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

s1 and s2 consist of lowercase English letters.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Sliding window + HashMap
        
        Permutation = exact same chars but different order
        --> check with HashMap
        
        Idea: looking for window of the same size as s1, 
        		containing same chars as s1.
        
        Passes the tests
        
        n - size s1, k - size s2
		
		26 - because s1 and s2 consist of lowercase English letters.
        
        Time: O(n) + O(k * n)
        Space: O(26) -- O(1)
        """

        if len(s1) > len(s2):
            return False
        
        if len(s1) == 1: return s1[0] in s2

        s1_len = len(s1)

        # Create count of s1 chars
        s1CharCount = {}
        for char in s1:
            s1CharCount[char] = 1 + s1CharCount.get(char, 0)


        for ind in range(0, len(s2) - s1_len + 1):
            cand_window = s2[ind: ind + s1_len]

            # Has window same chars as s1CharCount?
            if self.windowHasPermutation(cand_window, s1CharCount):
                return True

        return False
    
    def windowHasPermutation(self, cand_window, s1CharCount):
    	'''
    	Helper function to check if cand_window (str) contains same number of chars as in s1
    	'''
        
        windowCharCount = {}
        for char in cand_window:
            windowCharCount[char] = 1 + windowCharCount.get(char, 0)

        for char, count in windowCharCount.items():
            if char not in s1CharCount or s1CharCount[char] != count:
                return False

        return True


##########
#
##########
class TLESolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Sliding window + HashMap
        
        Hashmap - count of chars in s1
        Iterate over s2, if char in hashmap - check for potential substring (all subsequent chars appear in hashmap)
        
        <Time Limit Exceeded>
		
		n - size s1, k - size s2
		
		26 - because s1 and s2 consist of lowercase English letters.
		
        Time: O(n) + O(k * 26 * ?)
        Space: O(26) --> O(1)
        """

        if len(s1) > len(s2):
            return False

        s1_len = len(s1)

        # Create count of s1 chars
        s1CharCount = {}
        for char in s1:
            s1CharCount[char] = 1 + s1CharCount.get(char, 0)
        
        # Iterate over s2 & find permutation of s1
        for ind in range(len(s2)):
            
            substringChars = s1CharCount.copy()
            
            # case - substring start
            substring = ''
            i = ind
            while i < len(s2) and s2[i] in substringChars:
                if substringChars[s2[i]] > 0:
                    substringChars[s2[i]] -= 1
                    substring += s2[i]
                else:
                    break
                i += 1

            if len(substring) == s1_len:
                return True
    
        return False


