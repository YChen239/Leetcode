## 6. ZigZag Conversion ##

###  Description: ###
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string s, int numRows);
```

### Examples ###
#### Example1: ####
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

####  Example2: ####
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

### Solutions ###
#### Solution1: ####
Myself solution O(n^2) 40ms/11.8mb
```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zig = []
        n = 2*numRows-2
        m = 0
        if numRows>=len(s) or numRows==1:
            return s
        for i in range (numRows):
            temp = i
            zig.append(s[temp])
            while (temp+n)<len(s):
                if n !=0:
                    temp+=n
                    zig.append(s[temp])
                if m != 0:
                    if (temp+m)>=len(s):
                        break
                    temp+=m
                    zig.append(s[temp])
            n-=2
            m+=2
        zig = ''.join(zig)
        return zig
  ```
  
  #### Solution2: ####
  O(n) 28ms/11.8mb
  Simply like a sliding window. 
  ```python
  class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
  ```
