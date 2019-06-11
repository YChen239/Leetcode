## 21. Merge Two Sorted Lists ##
### Description: ###
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

### Example: ###
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

### Solution: ###
20ms/11.8mb
```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(0)
        while (l1 and l2):
            if l1.val<l2.val:
                cur.next = l1
                cur = cur.next
                l1 =l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return head.next
```
