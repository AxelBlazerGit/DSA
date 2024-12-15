#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        i=j=0
        while k>1 and i<len(a) and j<len(b):
            if a[i]<b[j]:
                i+=1
            else:
                j+=1
            k-=1
        if i < len(a) and j < len(b):
            return min(a[i], b[j])
        elif i < len(a):
            return a[i + k - 1]
        else:
            return b[j + k - 1]
