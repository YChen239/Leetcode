## 14. Longest Common Prefix ##
### Description: ###
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
### Examples: ###
#### Example1: ####
```
Input: ["flower","flow","flight"]
Output: "fl"
```
#### Example2: ####
```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```
**Note:**
All given inputs are in lowercase letters a-z.
### Solution: ###
|Time Complexity|Result|
|:---:|:---:|
|O(m+n)|20ms/12.1mb|
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        else:
            shortest = min(strs, key = len)
            for i, ch in enumerate(shortest):
                for other in strs:
                    if other[i]!=ch:
                        return shortest[:i]
            return shortest
```
