## 23. Merge k Sorted Lists ##
### Description: ###
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

### Example: ###
```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

### Solution: ###
```python
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return
        if len(lists)==1: return lists[0]
        if len(lists)==2:
            l1 = lists[0]
            l2 = lists[1]
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
        else: 
            return self.mergeKLists([self.mergeKLists(lists[:len(lists)/2]), self.mergeKLists(lists[len(lists)/2:])])
```
