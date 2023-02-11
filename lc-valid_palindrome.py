"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class ConstantMemorySolution:
    def isPalindrome(self, s: str) -> bool:
        """
        Do not use extra memory, work directly with input s.
        Use the same two-pointer technique to check if palindrome.
        If char is not alphanumeric --> move the pointer to the next char until both pointers at alphanumeric.
        
        Time - O(n)
        Space - O(1)
        """
		
        l = 0
        r = len(s) - 1
		
        while l < r:
            
            # Skip any non alphanumeric characters
            while (l < r) and not s[l].isalnum():
                l += 1
            while (l < r) and not s[r].isalnum():
                r -= 1

            # Check if elements at two pointers are the same
            if s[l].lower() != s[r].lower():
                return False

            # Update pointers to the next positions
            l += 1
            r -= 1
        
        return True


class ExtraMemorySolution:
    def isPalindrome(self, s: str) -> bool:
        """
        Idea: 1) convert to suitable representation
              2) use two-pointer technique (start, end) to check if palindrome
        
        Python trick - return alphanumeric_s == alphanumeric_s[::-1] # if string == reversed_string

        Time - O(n) 
        Space - O(n) to keep alphanumeric representation of s
        """
        
        # convert to alphanumeric representation
        alphanumeric_s = ''
        for char in s:
            if char.isalnum():
                alphanumeric_s += char.lower()
        
        # check if palindrome with two-pointer technique
        l = 0
        r = len(alphanumeric_s) - 1

        while l < r:
            if alphanumeric_s[l] != alphanumeric_s[r]:
                return False
                
            l += 1
            r -= 1

        return True

