class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        result = []
        i, j = 0, len(arr) - 1
        while i <= j:
            if i == j:
                result.append(arr[i])
            else:
                result.append(arr[j])
                result.append(arr[i])
            i += 1
            j -= 1
        
        return result
