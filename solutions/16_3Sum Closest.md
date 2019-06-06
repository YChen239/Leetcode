## 16. 3Sum Closest ##
### Description: ###
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

### Example: ###
```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
 
### Solution: ###
|Time Complexitmby|Result|
|:---:|:---:|
|![img](http://latex.codecogs.com/svg.latex?O%5Cleft%28n%5E2%5Cright%29)|72ms/11.8mb

Similar to NO.15.

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        curr = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if abs(val - target) < abs(curr - target):
                    curr = val
                if val == target:
                    return target
                elif val < target:
                    l += 1
                else:
                    r -= 1
        return curr
```
