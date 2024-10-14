#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        prefix = 0
        hash = {0: 1}
        count = 0
        for num in arr:
            prefix += num
            if prefix - tar in hash:
                count += hash[prefix - tar]
            if prefix in hash:
                hash[prefix] += 1
            else:
                hash[prefix] = 1
        return count
