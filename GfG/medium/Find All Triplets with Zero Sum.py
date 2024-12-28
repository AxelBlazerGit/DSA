# User function template for Python3
class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        temp = set()
        
        # (i, j) => arr[i] + arr[j] = sum
        hash = dict()

        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s not in hash:
                    hash[s] = list()

                hash[vis].append((i, j))
        
        # find third element
        for i in range(n):
            more = -arr[i]
            if more in hash:
                for idx in hash[more]:
                    if idx[0] != i and idx[1] != i:
                        triplet = sorted([i, idx[0], idx[1]])
                        temp.add(tuple(triplet))
        
        return [list(x) for x in temp]

# close by

# #User function Template for python3
# from collections import defaultdict
# class Solution:
#     def findTriplets(self, arr):
#         # Your code here
#         n=len(arr)
#         ans=[]
#         for i in range(len(arr)-2):
#             x=arr[i]
#             hash=defaultdict(list)
#             for j in range(i+1,len(arr)):
#                 y=arr[j]
#                 z=-(x+y)
#                 if z in hash:
#                     for idx in hash[z]:
#                         ans.append([i,idx,j])
#                 hash[y].append(j)
#         return ans
