## 5.Longest Palindromic Substring ##

### Description: ###
Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

### Examples: ###
#### Example1: ####
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
#### Example2: ####
```
Input: "cbbd"
Output: "bb"
```
### Solutions: ###
#### Solution1: ####

O(n^2), 836ms/11.7mb
```python
def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    res = ""
    if len(s)<2:
        return s

    else:
        for i in range(len(s)):
            even = self.PalinSub(i,i+1,s)
            old = self.PalinSub(i,i,s)
            temp = max(even, old, key=len)
            res = max(temp, res, key=len)
        return res

def PalinSub(self, r, l, s):
    while(r>=0 and l<len(s) and s[r]==s[l]):
        r-=1
        l+=1
    return s[r+1:l]
```

