"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        The close bracket must follow the last seen open bracket in order to be valid. 
        Keep track of the last open bracket --> Stack!

        Solution: use stack to keep all the opening brackets
                  if encounter close bracket, ckeck if it matches the last element in stack
        
        Time: O(n)
        Space: O(n)
        """

        # the closig bracket MUST match the last encountered opening bracket
        stack_open_brackets = []

        open_brackets = set(['(', '[', '{'])
        close_brackets = set([')', ']', '}'])

        mapping = {')': '(', ']':'[', '}':'{'}

        for bracket in s:
            if bracket in open_brackets:       # simply add open brackets to stack
                stack_open_brackets.append(bracket)
            elif bracket in close_brackets:    # close bracket MUST match the stack.pop() bracket to be valid
                if not stack_open_brackets:
                    return False
                
                stack_top_bracket = stack_open_brackets.pop()

                # Match?
                if mapping[bracket] != stack_top_bracket:
                    return False

        return True if not stack_open_brackets else False

