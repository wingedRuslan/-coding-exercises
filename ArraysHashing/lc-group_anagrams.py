"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	"""
    	Idea: introduce hashmap to group anagrams, where key - count of chars (all possible 26 letters) in string 
    	
    	Time - O(m * k)
    	Space - O(m)
    	m - len(strs), k - average len strings in strs
    	"""
        
        bucketAnagrams = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            # ! strs[i] consists of lowercase English letters
            charCount = [0] * 26

            for char in s:
                charCount[ord(char) - ord('a')] += 1
            
            # list can not be key --> tuple
            bucketAnagrams[tuple(charCount)].append(s)

        return bucketAnagrams.values()

