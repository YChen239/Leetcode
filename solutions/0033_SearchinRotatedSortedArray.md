## 33. Search in Rotated Sorted Array ##
### Description: ###
```
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
```
### Examples: ###
#### Example1: ####
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```
#### Example2: ####
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### Solutions: ###
Simple search O(n)

20ms/12.1mb
#### Solution1: ####
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target: return i
        return -1
```

#### Solution2: ####
Binary Search O(log(n))

28ms/12mb
```python
class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
```
