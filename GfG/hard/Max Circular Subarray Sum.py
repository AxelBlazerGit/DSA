#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    gmax=gmin=arr[0]
    curpos=curneg=total=0
    for i in arr:
        curpos=max(curpos+i,i)
        curneg=min(curneg+i,i)
        gmax=max(gmax,curpos)
        gmin=min(gmin,curneg)
        total+=i
    return max(gmax,total-gmin) if gmax>0 else gmax
