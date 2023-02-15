## Stack - Last-in-first-out Data Structure

In a LIFO data structure, the newest element added to the queue will be processed first. 
Different from the queue, the stack is a LIFO data structure. 
Similar to the queue, `push` - a new element is always added at the end of the stack. 
However, the delete operation, `pop`, will always remove the last element which is opposite from the queue.

Time complexities:
- `push()` - O(1)
- `pop()` - O(1)
- `top()` - O(1)

#### Stack Implementation
- dynamic array (**list()**) is sufficient to implement a stack structure. Built-in functions do the job for `push`, `pop`, `top` (via indexing). 
*Caveat*: lists are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.
- doubly linked list
- [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) - generalization of stacks and queues. Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

#### Stack Usage
- When you want to process the last element first, the stack will be the most appropriate data structure.
