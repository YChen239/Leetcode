## 22. Generate Parentheses ##
### Description: ###
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

### Solution: ###
16ms/12mb
```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def bfs(left, right, result, results = []):
            if left: bfs(left-1 ,right, result+'(')
            if right>left: bfs(left, right-1, result+')')
            if not right: 
                results.append(result)
            return results
        return bfs(n, n, '')
```
