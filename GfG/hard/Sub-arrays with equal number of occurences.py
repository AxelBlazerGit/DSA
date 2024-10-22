#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        ans=0
        hash={}
        hash[0]=1
        cnt=[0]*2
        for i in range(len(arr)):
            if arr[i]==x:
                cnt[0]+=1
            elif arr[i]==y:
                cnt[1]+=1
            difference=cnt[0]-cnt[1]
            if difference in hash:
                ans+=hash[difference]
            hash[difference]=hash.get(difference,0)+1
        return ans
