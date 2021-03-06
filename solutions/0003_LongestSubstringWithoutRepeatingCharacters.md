## 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

**Example 1:**
```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
```
**Example 2:**
```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
**Example 3:**
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Solution:**
* used simple search (52ms/12.6mb)
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        used = []
        for i in range (len(s)):
            if s[i] in used:
                if len(used)>maxlen:
                    maxlen = len(used)
                p = used.index(s[i])
                used = used[p+1:]
            used.append(s[i])          
            
        if len(used)>maxlen:
            maxlen = len(used)
            
        return maxlen
```

* used hash table(44ms/12.1mb)
```python
def lengthOfLongestSubstring(self, s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            # update the res
            res = max(res, i-start)
            # here should be careful, like "abba"
            start = max(start, dic[ch]+1)
        dic[ch] = i
    # return should consider the last 
    # non-repeated substring
    return max(res, len(s)-start)
 ```
