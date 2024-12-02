#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        n1=len(pat)
        pref=[0]*n1
        
        for i in range(1,n1):
            j=pref[i-1]
            
            while j>0 and pat[i]!=pat[j]:
                j=pref[j-1]
                
            if pat[i]==pat[j]:
                j+=1
                
            pref[i]=j
            
        kmp=list()
        i=j=0
        while i<len(txt):
            if txt[i]==pat[j]:
                i+=1
                j+=1
            elif j:
                j=pref[j-1]
            else:
                i+=1
            if j==n1:
                kmp.append(i-n1)
                j=pref[j-1]
                
        return kmp
