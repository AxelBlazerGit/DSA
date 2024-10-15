class Solution:
    def checkSorted(self, arr):
        #code here
        n = len(arr)
        temp = [(x+1) for x in range(n)]
        hash = [i for i in range(n) if arr[i] != temp[i]]
        
        if not hash:
            return True
        if len(hash) > 4:
            return False
        
        def swap(a, b, c):
            a[b[0]], a[b[1]] = a[b[1]], a[b[0]]
            a[c[0]], a[c[1]] = a[c[1]], a[c[0]]
            return a

        if len(hash) == 2:
            x, y = hash
            arr[x], arr[y] = arr[y], arr[x]
            return arr == temp
        
        if len(hash) == 4:
            x1, x2, y1, y2 = hash
            if swap(arr[:], [x1, x2], [y1, y2]) == temp:
                return True
            if swap(arr[:], [x1, y1], [x2, y2]) == temp:
                return True
            if swap(arr[:], [x1, y2], [x2, y1]) == temp:
                return True
        
        return False
