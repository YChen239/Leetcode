## 9. Palindrome Number ##
### Description: ###
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
### Examples: ###
#### Example1: ####
```
Input: 121
Output: true
```
#### Example2: ####
```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
#### Example3: ####
```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

### Solution: ###
44ms/11.7mb
```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False
        ret = 0
        ret =int(str(abs(x))[::-1])
        if ret == x: return True
        
        #one line solution: return x==int(str(abs(x))[::-1])
```
