#User function Template for python3


class Solution:

    def aggressiveCows(self, stalls, k):
        def cow(x):
            cur=1
            prev=stalls[0]
            for i in stalls[1:]:
                if i-prev>=x:
                    cur+=1
                    prev=i
                    if cur>=k:
                        return True
            return False
        stalls.sort()
        n=len(stalls)
        s=1
        e=stalls[-1]-stalls[0]
        while s<=e:
            m=(s+e)//2
            if cow(m):
                s=m+1
            else:
                e=m-1
        return e
