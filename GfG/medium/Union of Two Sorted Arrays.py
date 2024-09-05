class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        ptr1,ptr2=0,0
        ans=[]
        while(ptr1<n and ptr2<m):
            if(arr1[ptr1]<=arr2[ptr2]):
                if not ans:
                    ans.append(arr1[ptr1])
                elif ans[-1]!=arr1[ptr1]:
                    ans.append(arr1[ptr1])
                ptr1+=1
            else:
                if not ans:
                    ans.append(arr2[ptr2])
                elif ans[-1]!=arr2[ptr2]:
                    ans.append(arr2[ptr2])
                ptr2+=1
        while ptr1 < n:
            if ans[-1] != arr1[ptr1]:
                ans.append(arr1[ptr1])
            ptr1 += 1
        while ptr2 < m:
            if ans[-1] != arr2[ptr2]:
                ans.append(arr2[ptr2])
            ptr2 += 1
        return ans
