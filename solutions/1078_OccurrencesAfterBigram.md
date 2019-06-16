## 1078. Occurrences After Bigram ##
### Description: ###
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

### Examples: ###
#### Example1: ####
```
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
```
#### Example2: ####
```
Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
```

**Note:**

1. 1 <= text.length <= 1000
2. text consists of space separated words, where each word consists of lowercase English letters.
3. 1 <= first.length, second.length <= 10
4. first and second consist of lowercase English letters.


#### Solution: ####
O(n) 12ms/11.7mb
```python
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        t = text.split(' ')
        ret = []
        for i in range (len(t)-2):
            if t[i]==first and t[i+1]==second:
                ret.append(t[i+2])
        return ret
```
