"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise. 

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Keep track of char occurrences in s and t in two corresponding hashmaps
        Compare the number of every char occurrence in s with same statistic in t
        Time - O(n)
        Space - O(n)
        n - len(s) == len(t)
        """

        if len(s) != len(t): return False
        
        s_count, t_count = {}, {}
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        for char in s_count:
            if s_count[char] != t_count.get(char, -1):
                return False

        return True

