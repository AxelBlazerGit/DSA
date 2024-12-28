from collections import Counter
class Solution:
    def intersect(self,hash,arr):
        commons=set()
        for i in arr:
            if i in hash:
                commons.add(i)
        return list(commons)
    def freq(self,arr):
        return set(arr)
    def intersectionWithDuplicates(self, a, b):
        # code here
        if len(a) < len(b):
            hash = self.freq(a)
            return self.intersect(hash, b)
        return self.intersect(self.freq(b), a)
