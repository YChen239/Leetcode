## 17. Letter Combinations of a Phone Number ##
### Description: ###
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

### Example: ###
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
**Note:**
Although the above answer is in lexicographical order, your answer could be in any order you want.

### Solution: ###
12ms/11.7mb
```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'nmo', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits)==0:
            return []
        if len(digits)==1:
            return dic[digits]
        else:
            prev = self.letterCombinations(digits[:-1])
            add = digits[-1]
            return[s+r for s in prev for r in dic[add]]
```
