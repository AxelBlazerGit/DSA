#User function Template for python3

class Solution:
    def subArraySum(self,arr,k):  
        #code here
        hash = {0: 1}
        prefix = 0
        count = 0
        for num in arr:
            prefix += num
            if prefix - k in hash:
                count += hash[prefix - k]
            if prefix in hash:
                hash[prefix] += 1
            else:
                hash[prefix] = 1
        
        return count
