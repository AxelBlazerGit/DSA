def leaders(self,n, arr):
        #Code here
        leads=[arr[-1]]
        for i in range(n-1,-1,-1):
            if arr[i]>=leads[-1]:
                leads.append(arr[i])
        return leads[1:][::-1]
