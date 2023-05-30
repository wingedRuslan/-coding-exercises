"""
Description
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.  
Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Input: the list [[1,1],2,[1,1]], 
Output: 10. 
Explanation:
four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10


Input: the list [1,[4,[6]]], 
Output: 27. 
Explanation:
one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27
"""


def getWeightedSum(nestedList):
    """
    Breadth-first search algorithm.
    
    1) Add el of input to queue as (el, depth=1)
    2) Process each el in queue:
        - if int --> remove from queue, update sum
        - if list --> add each el of list to the add of queue && increase the depth += 1
    
    Time - O(k*n), k - average depth of the elements in the nestedList
    Space - O(n)
    """
    
    if len(nestedList) == 0:
        return 0
    
    # Add each el of input list to stack (el, depth=1)
    queue = []
    for i in nestedList:
        queue.append((i, 1))
    
    weightedSum = 0

    # Process each el in stack
    while queue:
        
        # Get the el from stack FIFO
        element, depth = queue.pop(0)
        
        if isinstance(element, int):        # remove from queue
            weightedSum += element * depth
        elif isinstance(element, list):     # nested list elements add to queue & depth+1
            for i in element:
                queue.append((i, depth+1))
    
    return weightedSum



res = getWeightedSum(nestedList=[[1,1], 2, [1,1]])
print(res)
