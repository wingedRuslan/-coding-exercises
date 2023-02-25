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


### Two Pointer Technique

Use two pointers with different speed in a linked list.

e.g. in Linked List Cycle:  
If there is no cycle, the fast pointer will stop at the end of the linked list.  
If there is a cycle, the fast pointer will eventually meet with the slow pointer.  


### Singly linked list and Doubly linked list

They are **similar** in many operations:
- Both of them are not able to access the data at a random position in constant time.
- Both of them can add a new node after given node or at the beginning of the list in O(1) time.
- Both of them can delete the first node in O(1) time.

But it is a little different to delete a given node (including the last node).

- In a singly linked list, it is not able to get the previous node of a given node so we have to spend O(N) time to find out the previous node before deleting the given node.
- In a doubly-linked list, it will be much easier because we can get the previous node with the "prev" reference field. So we can delete a given node in O(1) time.


### Comparison of time complexity between the linked list and the array
![image](https://user-images.githubusercontent.com/14000852/221376985-87d2fac3-0cde-4487-acb7-481076e37b88.png)

*Note*: The given time complexities for the Doubly-Linked List assume that the Doubly-Linked List implementation keeps a reference to the tail node. If a reference to the tail node is not kept, then adding a node after the last node or deleting the last node would also require O(N) time.

**Conclusion**:  
> If you need to add or delete a node frequently, a linked list could be a good choice.  
> If you need to access an element by index often, an array might be a better choice than a linked list.  
