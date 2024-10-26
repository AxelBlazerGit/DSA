class Solution:
    def findTriplet(self, arr):
        n=len(arr)
        for i in range(n):
            target = arr[i]
            seen = set()
            for j in range(n):
                if i != j:
                    needed = target - arr[j]
                    if needed in seen:
                        return True
                    seen.add(arr[j])
        
        return False
