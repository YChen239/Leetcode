## 4. Median of Two Sorted Arrays ##

### Description ###

There are two sorted arrays **nums1** and **nums2** of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume **nums1** and **nums2** cannot be both empty.

### Examples ###
**Example1:**
```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

**Example2:**
```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

### Solutions ###

#### Solution1: ####

Use O(min(n, m)) **72ms/11.8mb**
```python
def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = 0
    n = 0
    cum = []
    for i in range((len(nums1)+len(nums2))):
        if m<len(nums1) and n<len(nums2):
            if nums1[m] < nums2[n]:
                cum.append(nums1[m])
                m+=1
            else:
                cum.append(nums2[n])
                n+=1
        elif m<len(nums1):
            cum.append(nums1[m])
            m+=1
        elif n<len(nums2):
            cum.append(nums2[n])
            n+=1
        else:
            break

    if len(cum)%2:
        return cum[len(cum)//2]
    else:
        return float(cum[len(cum)//2-1]+cum[len(cum)//2])/2
```

### Solution2: ###
Binaray Search O(log(min(n,m))) **76ms/12mb**
```python
def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        #nums1[-1] == -float('inf'), nums1[len1] == float('inf)
        nums1 += [float('inf'), -float('inf')]
        #nums2[-1] == -float('inf'), nums2[len2] == float('inf)
        nums2 += [float('inf'), -float('inf')]
        left = 0
        right = len1
        i = len1
        j = (len1 + len2) // 2 - i
        while max(nums1[i-1], nums2[j-1]) > min(nums1[i], nums2[j]):
            if nums1[i-1] > nums2[j]:
                right = i - 1
            else:
                left = i + 1
            i = (left + right) // 2
            j = (len1+ len2) // 2 - i
        if (len1 + len2) % 2 == 0:
            return (max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])) / 2.0
        return min(nums1[i], nums2[j])
```
