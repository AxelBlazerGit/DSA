#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        ans=1
        curr=height[0]
        for i in height[1:]:
            if i>curr:
                ans+=1
                curr=i
        return ans
