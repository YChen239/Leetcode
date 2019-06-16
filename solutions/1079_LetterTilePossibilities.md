## 1079. Letter Tile Possibilities ##
### Description: ###
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

### Examples: ###
#### Example1: ####
```
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
```

#### Example2: ####
```
Input: "AAABBC"
Output: 188
```

**Note:**

1. 1 <= tiles.length <= 7
2. tiles consists of uppercase English letters.

### Solution: ###
find all possible sequences and use set to move repeated one.

44ms/13.9mb
```python
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = {''}
        for c in tiles:
            res |= {d[:i] + c + d[i:] for d in res for i in range(len(d)+1)}
        return len(res) - 1
```
