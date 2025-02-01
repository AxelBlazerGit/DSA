# Enter your code here. Read input from STDIN. Print output to STDOUT
from bisect import bisect_left
n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
def f(n,arr):
    arr.sort(key=lambda x:(x[0],-x[1]))
    ans=[]
    for a,h in arr:
        posn=bisect_left(ans, h)
        if posn==len(ans):
            ans.append(h)
        else:
            ans[posn] = h
    print(len(ans))
f(n,arr)
# In a grand royal palace, there is a treasure trove filled with a collection of luxurious jewelry boxes. Each box has a specific width and height, and the queen wants to store them in a special way.

# The queen loves stacking jewelry boxes, but there is a rule: a jewelry box can only fit inside another box if both its width and height are strictly smaller than the width and height of the other box. The goal is to determine the maximum number of jewelry boxes that can be nested inside each other in a single stack, such that each box is strictly smaller than the one placed above it.

# The queen has asked you to help her figure out the maximum number of jewelry boxes she can stack in a sequence that follows this rule.

# You are given a list jewelry_boxes where each element is a pair of integers [wi, hi] representing the width and height of a jewelry box. Your task is to determine the maximum number of jewelry boxes that can be nested.

# Input Format

# An integer n denoting number of pairs
# n pairs of two space separated integers where each pair [wi, hi] represents the width and height of a jewelry box.
# Each pair of integers represents a unique jewelry box.
# Constraints

# 1 ≤ jewelry_boxes.length ≤ 10^5
# jewelry_boxes[i].length == 2
# 1 ≤ wi, hi ≤ 10^5
# Output Format

# Return a single integer — the maximum number of jewelry boxes that can be nested inside each other.
# Sample Input 0

# 4
# 5 4 
# 6 4 
# 6 7
# 2 3
# Sample Output 0

# 3
# Explanation 0

# The maximum number of jewelry boxes that can be stacked is 3, where the boxes are nested in this order: [2, 3] -> [5, 4] -> [6, 7].

# Sample Input 1

#  3
#  1 1
#  1 1
#  1 1
# Sample Output 1

# 1
# Explanation 1

# Since all the jewelry boxes are identical, none can fit inside another, so the maximum number of boxes you can nest is just one.
