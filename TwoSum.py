## First way with O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums [j] == target:
                    a = i
                    b = j
        
        return [a,b]
