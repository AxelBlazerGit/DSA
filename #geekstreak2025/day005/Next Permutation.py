#User function Template for python3

class Solution:
    
    def nextPermutation(self, arr):
        # code here
        def rev(s,e):
            while s<e:
                arr[s],arr[e]=arr[e],arr[s]
                s+=1
                e-=1
                
        n=len(arr)
        i=n-2
        
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
            
        if i>=0:
            j=n-1
            
            while arr[j]<=arr[i]:
                j-=1
                
            arr[i],arr[j]=arr[j],arr[i]
            
        rev(i+1,n-1)
        
        return arr
