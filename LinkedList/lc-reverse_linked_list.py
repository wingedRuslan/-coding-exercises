# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class RecursiveSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive solution
            --> break it down into subproblems
                --> instead of reversing the entire linked list, reverse all the nodes after head (the reminder of the list)
        
        head - plays the role pf {prev} in a way.
        newHead - keeps the last element of linked list; in reversed list it is a new head

        Time - O(n)
        Space - O(n) - to keep recursive calls
        (in iterative it is constant)
        """
        
        # Base case
        if head is None:
            return None
        
        # Maintain the last node as the new head to return
        newHead = head
        
        # if there is still a subproblem; if we can keep reversing
        if head.next is not None:
            newHead = self.reverseList(head.next)    # find the very last element and keep it in newHead
            head.next.next = head                    # reverse the link between head and head.next (the next node)
        
        head.next = None

        return newHead


class IterativeSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	"""
    	Use two pointers: prev and curr while iterating through array with curr.
    	
    	Init prev - None
    	For each node, take the next pointer and reverse it --> point to {prev}
    	Shift the two pointers
    	
    	Subproblem that is needed in other linkedlist related problems.
    	
    	Time - O(n)
    	Space - O(1)
    	"""

        if head is None:
            return None

        prev = None
        curr = head

        while curr is not None:
            
            # Reverse the pointers of two adjacent nodes [1] -> [2] ... [1] <- [2]
            nxt = curr.next
            curr.next = prev
			
            # Move pointers
            prev = curr
            curr = nxt
		
		# prev - new head        
        return prev

