## 10. Regular Expression Matching ##
### Description: ###
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```
The matching should cover the entire input string (not partial).

**Note:**
* s could be empty and contains only lowercase letters a-z.
* p could be empty and contains only lowercase letters a-z, and characters like . or *.

### Examples: ###
#### Example1: ####
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```
#### Example2: ####
```
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```
#### Example3: ####
```
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```
#### Example4: ####
```
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
```
#### Example5: ####
```
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

### Solutions: ###
#### Solution1: ####
Usw the trick in python it self
56ms.11.8mb
```python
import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        result = re.match(p, s)
        if result and result.start() == 0 and result.end() == len(s):
            return True
        return False
```

#### Solution2: ####
Use recurion.

|Time complexity|Result|
|:----:|:---:|
|![img](http://latex.codecogs.com/svg.latex?O%5Cleft%28%5Cleft%28T%2BP%5Cright%292%5E%7BT%2B%5Cfrac%7BP%7D%7B2%7D%7D%5Cright%29)| 1024ms/12mb|

The rule is:
1. When the length of p is equal to 0, returen len(s)==0;
2. When the length of p is equal to 1, s should be '.' or s[0]==p[0];
3. When the length of p is longger than 1, we should consider 's':
    1. if p[1] is not euqal to '*', we can return true when the first two pattern is matched as well as the rest.
    2. if p[1] is equal to '*', we should consider all possible times that s[0] repeats.
    
```python
        #Simple use recursion
        if len(p)==0: return len(s)==0
        if len(p)==1:
            return len(s)==1 and (p[0]=='.' or p[0]==s[0])
        if p[1]!='*':
            return len(s) !=0 and(p[0]=='.' or p[0]==s[0]) and self.isMatch(s[1:],p[1:])
        else:
            while (len(s) !=0 and(p[0]=='.' or p[0]==s[0])):
                if self.isMatch(s,p[2:]):
                    return True
                else:
                    s=s[1:]
            return self.isMatch(s,p[2:])
```
#### Solution3: ####
|Time complexity|Result|
|:----:|:---:|
|![img](http://latex.codecogs.com/svg.latex?O%5Cleft%28n%5E2%5Cright%29)| 36ms/11.8mb|

Use DP to solve the problem.

```python
dp = [[True] + [False] * len(s)]
for i, pc in enumerate(p):
    row = [pc == '*' and dp[-2][0]]
    for j, sc in enumerate(s):
        if pc == '.':
            row.append(dp[-1][j])
        elif pc == '*':
            row.append(dp[-2][j + 1] or ((p[i - 1] == '.' or p[i - 1] == sc) and row[j]))
        else:
            row.append(dp[-1][j] and pc == sc)
    dp.append(row)
return dp[-1][-1]
```
