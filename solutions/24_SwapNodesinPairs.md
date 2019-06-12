## 24. Swap Nodes in Pairs ##
### Description: ###
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

### Example: ###
```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

### Solution: ###
16ms/11.8mb
```python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        cur.next = head
        while(cur.next and cur.next.next):
            a = cur.next
            b = a.next
            cur.next = b
            a.next = b.next
            b.next = a
            cur = a
            
        return dummy.next
```
