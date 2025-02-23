#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #Your code here
        candidate=-1
        vote=0
        for ele in arr:
            if not vote:
                candidate=ele
                vote=1
            else:
                if ele==candidate:
                    vote+=1
                else:
                    vote-=1
        vote=0
        for i in arr:
            if i==candidate:
                vote+=1
        return candidate if vote>len(arr)//2 else -1
