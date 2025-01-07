#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
            i = 0
            j = len(arr) - 1
            ans = 0
        
            while i < j:
                s = arr[i] + arr[j]
                if s == target:
                    if arr[i] == arr[j]:
                        temp = j - i
                        ans += (temp * (temp + 1)) // 2
                        break
                    else:
                        left = 1
                        right = 1
                        while i < j and arr[i] == arr[i + 1]:
                            left += 1
                            i += 1
                        while i < j and arr[j] == arr[j - 1]:
                            right += 1
                            j -= 1
                        ans += (left * right)
                        i += 1
                        j -= 1
                elif s < target:
                    i += 1
                else:
                    j -= 1
        
            return ans
