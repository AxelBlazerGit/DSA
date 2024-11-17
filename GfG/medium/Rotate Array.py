#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        def reverse(s,e):
            while s<e:
                arr[s],arr[e]=arr[e],arr[s]
                s+=1
                e-=1
        d%=len(arr)
        reverse(0,d-1)
        reverse(d,len(arr)-1)
        reverse(0,len(arr)-1)
        return arr
