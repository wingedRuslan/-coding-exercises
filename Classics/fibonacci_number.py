"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
"""


##########
# Optimized Recursion Approach
##########
class Solution:

    # Keep the intermediate calculations
    # Init w/ base cases results
    memoization = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
    	"""
    	Keep the intermediate results in the dict. (memoization technique)
    		--> for each i = 0..n - calculate fibonacci just one.
    	
    	Time: O(n)
    	Space: O(n)
    	"""

        if n in self.memoization:
            return self.memoization[n]
        
        self.memoization[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.memoization[n]


##########
# Naive Recursion Approach
##########
class NaiveRecursionSolution:
    def fib(self, n: int) -> int:
        """
        Naive Recursion Solution

        Time: O(2^n)
        Space: O(n) - keep the recursion calls
        """
        
        # Base Cases
        if n == 0: return 0
        if n == 1: return 1

        return self.fib(n-1) + self.fib(n-2)


##########
# Iterative Approach
##########
class IterativeSolution:
    def fib(self, n: int) -> int:
        """
        Every next number - sum of previous two numbers.
        --> keep 2 previous numbers in dynamic array
        0, 1 --> 1
           1, 1 --> 2
              1, 2 --> 3
        
        Time: O(n)
        Space: O(1) - keep only the previous 2 elements
        """
        prev_els = [0, 1]

        if n < 2:
            return prev_els[n]
        
        for i in range(2, n + 1):
            prev_els[0], prev_els[1] = prev_els[1], sum(prev_els)
        
        return prev_els[-1]


