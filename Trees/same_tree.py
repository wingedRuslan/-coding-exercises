"""
Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
"""

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        DFS Algo

        Same Trees iff
        - root1.val == root2.val
        - root1.left == root2.left
        - root1.right == root2.right

        Time: O(p + q), size of both trees added together
        Space: O(p + q)
        """

        # Base Case
        if not p and not q:
            return True
        
        # If one is None, other not None (or) values do not match
        if (not p or not q) or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

