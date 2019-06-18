## 32. Longest Valid Parentheses ##
### Description: ###
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

### Examples: ###
#### Example1: ####
```
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
```
#### Example2: ####
```
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

### Solution: ###
36ms/12.1mb
```python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0] #set initial record
        longest = 0
        
        for c in s:
            print(stack)
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2 #every pair count as two and add to record stack
                    longest = max(longest, stack[-1])
                else:
                    stack = [0] #For the situation when s[0]==')'

        return longest
```
