## 1071. Greatest Common Divisor of Strings ##
### Description: ###
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

### Examples: ###
#### Example1: ####
```
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```
#### Example2: ####
```
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```
#### Example3: ####
```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```
#### Note: ####
* 1 <= str1.length <= 1000
* 1 <= str2.length <= 1000
* str1[i] and str2[i] are English uppercase letters.

### Solutions: ###
16ms/11.8mb
```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)
        
        i = len1
        while i >= 1:
            print(i)
            if len1%i == 0 and len2%i == 0:
                break
            i = i-1
                
        if str1[:i] == str2[:i]:
            return str1[:i]
        else:
            return ''
```
