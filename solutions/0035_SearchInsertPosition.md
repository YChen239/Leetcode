## 35. Search Insert Position ##
### Description: ###
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

### Examples: ###
#### Example1: ####
```
Input: [1,3,5,6], 5
Output: 2
```
#### Example2: ####
```
Input: [1,3,5,6], 2
Output: 1
```

#### Example3: ####
```
Input: [1,3,5,6], 7
Output: 4
```

#### Example4: ####
```
Input: [1,3,5,6], 0
Output: 0
```

### Solutions: ###
#### Solution1: ####
O(n)
```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ##O(n)
        for i, v in enumerate(nums):
            if v>=target: return i
        return i+1
```

#### Solution2: ####
O(log(n))
```python
l , r = 0, len(nums)-1
while l <= r:
    mid=(l+r)/2
    if nums[mid]== target:
        return mid
    if nums[mid] < target:
        l = mid+1
    else:
        r = mid-1
return l
```
