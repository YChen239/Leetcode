## 1089. Duplicate Zeros ##
### Description: ###
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

### Examples: ###
#### Example1: ####
```
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
```
#### Example2: ####
```
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
```

### Solution: ###
76ms/12mb
```python
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        l = len(arr)
        while(i<l):
            if arr[i]==0:
                arr.insert(i,0)
                i+=1
            i+=1
        del arr[l:]
```
