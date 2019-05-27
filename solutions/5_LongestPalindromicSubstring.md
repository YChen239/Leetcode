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

DP: O(n^2), 836ms/11.7mb
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

#### Solution2: ####

O(n) 60ms/11.8mb
```python
def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
```


