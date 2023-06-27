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


class DPSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        2D DP Bottom-Up Solution

        Save observation as in BruteForce recursive solution: 
            -> Split the problem into subproblems!

        w1 = 'abd' - i
        w2 = 'acd' - j

        if w1[i] == w2[j]:
            move pointers (i+1, j+1) & check substrings
        else:
            insert: move pointers (i, j+1) & check substrings
            delete: move pointers (i+1, j) & check substrings
            replace: move pointers (i+1, j+1) & check substrings
        
        Idea: introduce a 2D array (columns - word2 (j), rows - word1 (i) )
        - at each cell (i,j): 
            store the min number of operations to get word1[i:] -> word2[j:]
        - additional dimension to strings - empty strings - base cases
        - start from the end of both strings at pos: [n, m]
        - populate the rows starting from the end
        - if current chars at [i] and [j] - equal - get the res from diagonal
        - if not: min(diagonal, down, right) + 1
        - final result at pos: [0, 0]

        |   | A | C | D |'' |
        |---|---|---|---|---|
        | A |   |   |   | 3  |
        | B |   |   |   | 2  |
        | D | 2  | 1  | 0  | 1  |
        | ''| 3  | 2  | 1  | 0  |


        |   | A | C | D |'' |
        |---|---|---|---|---|
        | A | 1  | 2  | 2  | 3  |
        | B | 2  | 1  | 1  | 2  |
        | D | 2  | 1  | 0  | 1  |
        | ''| 3  | 2  | 1  | 0  |


        Time: O(m * n), sizes of two strings
        Space: O(m * n), to keep the 2D array
        """

        # Create 2D array
        # cache[i][j] ~ min # of operations to convert word1[i:] to word2[j:]
        cache = [ [float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1) ]

        # Init base cases of 2D array - either of word1, word2 - empty strings
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i 

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        # DP - Bottom-Up solution
        # start from bottom row and end at the top row
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j + 1], # replace
                                          cache[i + 1][j],     # delete
                                          cache[i][j + 1])     # insert
        
        return cache[0][0]


class BruteForceSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        BruteForce solution - recursion on all possible ways how to word1 -> word2

        If first characters of two strings are same, nothing much to do. 
            Ignore first characters and get count for remaining strings.

        If first characters are not same, consider all three operations on first character of first string, 
            recursively compute minimum cost for all three operations and take minimum of three values.

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



