"""
Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""


class BruteForceSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        BruteForce solution - recursion on all possible ways how to word1 -> word2

        Time: O(3^n)
        Space: O(n)
        """
        
        # Base case - insert all chars from word2 to match word2
        if len(word1) == 0:
            return len(word2)
        
        # Base case - delete all chars from word1 to match word2
        if len(word2) == 0:
            return len(word1)

        # Recursively 
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            insert_cost = 1 + self.minDistance(word1, word2[1:])
            delete_cost = 1 + self.minDistance(word1[1:], word2)
            replace_cost = 1 + self.minDistance(word1[1:], word2[1:])

        return min(insert_cost, delete_cost, replace_cost)

