# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Two-Pointer Technique:

        Imagine there are two runners with different speed. 
        If they are running on a straight path, the fast runner will first arrive at the destination. 
        However, if they are running on a circular track, the fast runner will catch up with the slow runner if they keep running.

        Time - O(n)
        Space - O(1)

        BruteForceSolution: keep adding visited nodes into HashSet while iterating through list. Space - O(n)
        """

        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            
            # No cycle exist
            if fast.next is None or fast.next.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

