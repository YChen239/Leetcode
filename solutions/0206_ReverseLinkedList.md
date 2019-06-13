## 25. Reverse Nodes in k-Group ##
### Description: ###
Reverse a singly linked list.
### Example: ###
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
**Follow up**

A linked list can be reversed either iteratively or recursively. Could you implement both?

### Solutions: ###

iterative:

23ms/13.6mb
```python
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev
```

recursive:

32ms/18.5mb
```python
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)
```
