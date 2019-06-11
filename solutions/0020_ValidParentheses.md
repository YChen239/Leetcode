## 20. Valid Parentheses ##
### Descriotion: ###
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
  
Note that an empty string is also considered valid.
### Examples: ###
#### Example1: ####
```
Input: "()"
Output: true
```
#### Example2: ####
```
Input: "()[]{}"
Output: true
```
#### Example3: ####
```
Input: "(]"
Output: false
```
#### Example4: ####
```
Input: "([)]"
Output: false
```
#### Example5: ####
```
Input: "{[]}"
Output: true
```

### Solution: ###
O(n) 24ms/12mb
```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
```
