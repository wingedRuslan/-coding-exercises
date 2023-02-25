## Linked List

[Link to leetcode explore card](https://leetcode.com/explore/learn/card/linked-list/)

Similar to the array, the linked list is also a linear data structure. 
Each element in the linked list is actually a separate object while all the objects are linked together by the reference field in each element.

There are two types of linked list: singly linked list and doubly linked list.  

Each node in a singly-linked list contains not only the value but also a reference field to link to the next node. 
By this way, the singly-linked list organizes all the nodes in a sequence.

```
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

*Note*: In most cases, we will use the head node (the first node) to represent the whole list. 

### Operations

- Access element - O(n). Unlike the array, we are not able to access a random element in a singly-linked list in constant time. 
If we want to get the ith element, we have to traverse from the head node one by one. It takes us O(N) time on average to visit an element by index, where N is the length of the linked list.


*Note*: You might wonder why the linked list is useful though it has such a bad performance (compared to the array) in accessing data by index. The benefit of the linked list in the insert and delete operations.

- Insert - O(1). Unlike an array, we don’t need to move all elements past the inserted element. Therefore, you can insert a new node into a linked list in O(1) time complexity, which is very efficient.
- Delete - O(n). Need to find out prev and next nodes to the cur to be removed. It is easy to find out next using the reference field of cur. However, we have to traverse the linked list from the head node to find out prev which will take O(N) time on average, where N is the length of the linked list. So the time complexity of deleting a node will be O(N).
