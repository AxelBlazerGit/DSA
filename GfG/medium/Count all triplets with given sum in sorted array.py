
class Solution:
    def countTriplets(self, arr, target):
        # code here
        trips=0
        n=len(arr)
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                temp=arr[i]+arr[j]+arr[k]
                if temp<target:
                    j+=1
                elif temp>target:
                    k-=1
                else:
                    trips+=1
                    l=j+1
                    while l<k and arr[l]==arr[l-1]:
                        trips+=1
                        l+=1
                    k-=1
        return trips
