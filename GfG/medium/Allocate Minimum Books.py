class Solution:
    def possible(self, mid, pages, count):
        curr = 0
        partition = 1
        for i in range(len(pages)):
            if curr + pages[i] <= mid:
                curr += pages[i]
            else:
                partition += 1
                curr = pages[i]
        return partition <= count
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        if len(arr) < k:
            return -1
        s = max(arr)
        e = sum(arr)
        ans = -1
        while s <= e:
            mid = (s + e) // 2
            if self.possible(mid, arr, k):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        return ans
