t=int(input())
n=int(input())
arr=list(map(int,input().split()))
def f(t,n,arr):
    l,cur,ans=0,0,float('inf')
    for r in range(n):
        cur+=arr[r]
        while cur>=t:
            ans=min(ans,r-l+1)
            cur-=arr[l]
            l+=1
    return ans if ans!=float('inf') else 0
print(f(t,n,arr))
# In the mystical land of Sumoria, a hidden treasure lies buried deep within the Enchanted Valley. However, the treasure cannot be found easily—it requires the gathering of magical energy from a series of energy crystals scattered along a winding path.

# The energy of each crystal is represented as a positive number in an array. To uncover the treasure, you must gather enough energy to meet or exceed a certain target. The path to the treasure is tricky, as the crystals are scattered in a way that may require you to traverse several stretches of the path before reaching the needed energy.

# But there’s a catch—the treasure hunters of Sumoria have a saying: "The shortest path is the wisest path." This means that your goal is to find the shortest stretch of consecutive crystals that provides enough energy to meet or exceed the target. But beware—if no such stretch exists, the treasure will remain hidden, and you will return empty-handed.

# Input Format

# A single integer target — the target magical energy to uncover the treasure.
# An integer n — the number of crystals.
# n space separated integers, where each element represents the energy of a crystal.
# Constraints

# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# Output Format

# A single integer — the length of the shortest stretch of consecutive crystals that meets or exceeds the target energy. If no such stretch exists, output 0.
# Sample Input 0

# 7
# 6
# 2 3 1 2 4 3
# Sample Output 0

# 2
# Explanation 0

# The shortest stretch of crystals that meets or exceeds the target energy of 7 is [4, 3], which has a total energy of 7.

# Sample Input 1

# 4
# 3
# 1 4 4
# Sample Output 1

# 1
# Explanation 1

# The shortest stretch of crystals that meets or exceeds the target energy of 4 is [4], with a total energy of 4.

# Sample Input 2

# 11
# 8
# 1 1 1 1 1 1 1 1
# Sample Output 2

# 0
# Explanation 2

# No stretch of crystals contains enough energy to meet the target of 11, so the treasure remains out of reach.
