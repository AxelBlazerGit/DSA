#User function Template for python3
# from bisect import bisect_left
class Solution:
    def sumClosest(self, arr, target):
        # code here
        if len(arr)==1:
            return []
        arr.sort()
        if len(arr)==2:
            return arr
        s=0
        e=len(arr)-1
        delta=4*(10**5)
        x=y=-1
        while s<e:
            sm=arr[s]+arr[e]
            if delta>abs(target-sm):
                delta=abs(target-sm)
                x=arr[s]
                y=arr[e]
            elif delta==abs(target-sm):
                if arr[e]-arr[s]>y-x:
                    x=arr[s]
                    y=arr[e]
            if sm<target:   s+=1
            else:   e-=1
        return [x,y]
