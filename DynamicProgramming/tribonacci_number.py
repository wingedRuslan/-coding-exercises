'''
N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
'''

##########
# Optimized Recursive Approach
##########
class OptimizedRecursiveSolution:

    memory = {0:0, 1:1, 2:1}

    def tribonacci(self, n: int) -> int:
        """

        Time: O(n)
        Space: O(n)
        """

        if n in self.memory:
            return self.memory[n]
        
        self.memory[n] = self.tribonacci(n-1) +\
                         self.tribonacci(n-2) +\
                         self.tribonacci(n-3)
        
        return self.memory[n]


##########
# Naive Recursive Approach
##########
class NaiveRecursiveSolution:
    def tribonacci(self, n: int) -> int:
        """

        Time: O(3**n)
        Space: O(n)
        """
        
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)


##########
# Iterative Approach
##########
class IterativeSolution:
    def tribonacci(self, n: int) -> int:
        """
        Every next number - sum of previous three numbers.
        --> keep 3 previous numbers in dynamic array
        0, 1, 1 --> 2
           1, 1, 2 --> 4
              1, 2, 4 --> 7

        Time: O(n)
        Space: O(1)
        """
        t = [0, 1, 1]   # base cases

        if n < 3:
            return t[n]
        
        for i in range(3, n + 1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)

        return t[-1]


