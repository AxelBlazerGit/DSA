#User function Template for python3
class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        new=[min(a[0],b[0])]
        i=j=0
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                if a[i]!=new[-1]:
                    new.append(a[i])
                i+=1
            else:
                if b[j]!=new[-1]:
                    new.append(b[j])
                j+=1
        while i<len(a):
            if a[i]!=new[-1]:
                new.append(a[i])
            i+=1
        while j<len(b):
            if b[j]!=new[-1]:
                new.append(b[j])
            j+=1
        return new
