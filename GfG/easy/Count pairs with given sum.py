#User function Template for python3

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        pairs=0
        hash=collections.defaultdict(int)
        for i in arr:
            if hash[target-i]>0:
                pairs+=min(hash[i],hash[target-i])
            hash[i]+=1
        return pairs
