## 7. Reverse Integer ##
### Description: ###
Given a 32-bit signed integer, reverse digits of an integer.

**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

### Examples: ###
#### Example1: ####
```
Input: 123
Output: 321
```
#### Example2: ####
```
Input: -123
Output: -321
```
#### Example3: ####
```
Input: 120
Output: 21
```

### Solutions: ###
#### Solution1: ####
Simplest on written by myself.
24ms/11.8,b
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = abs(x)
        res = 0
        while (num):
            temp = num%10
            num = num/10
            res = res*10+temp
        if res>(2**31-1) or res<-2**31:
            return 0
        if x < 0:
            return -res
        else:
            return res
```

#### Solution2: ####
shortest one 12ms/11.7mb

The notation that is used in a[::-1] means

**<object_name>[<start_index>, <stop_index>, <step>]**
```python
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    sign = [1,-1][x < 0]
    rst = sign * int(str(abs(x))[::-1])
    return rst if -(2**31)-1 < rst < 2**31 else 0
```
