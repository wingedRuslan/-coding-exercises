"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:
    """
    Hint: Consider each position (node) in the stack having a minimum value.

    Define two stacks: 1. Stack (normal) - the values we added so far
                       2. Stack (minVal at each node) - stores the min val we added so far

    You must implement a solution with O(1) time complexity for each function. - [Done]
    """

    def __init__(self):
        self.stack = []  
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)    # add val at the end of the list

        # Is {val} < the min value at previous node (top of minStack)?
        # val - min(input val and the min at the top of minStack)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()        # remove an element from the last position in the list    
        self.minStack.pop()     # update minStack too!

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

