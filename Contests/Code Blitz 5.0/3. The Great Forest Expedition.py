n=int(input())
arr=list(map(int, input().split()))
def f(n,arr):
    res=[1]*n
    pref=1
    for i in range(n):
        res[i]=pref
        pref*=arr[i]
    suf=1
    for i in range(n-1,-1,-1):
        res[i]*=suf
        suf*=arr[i]
    print(" ".join(map(str, res)))
f(n,arr)
# The Kingdom of Arborville had long been known for its enchanted forests, sprawling mountains, and pristine rivers. Every year, the kingdom hosted a great expedition, where adventurers from all across the land would team up and venture into the heart of the mystical forest to uncover its ancient secrets.

# In this year's expedition, each group of adventurers had to work together to navigate through the forest, solve riddles, and face mythical creatures. However, there was one peculiar challenge that each adventurer had to tackle. As part of the team, every adventurer needed to calculate the product of the team's strength, excluding their own strength.

# You are given an array strengths, where strengths[i] represents the strength of the i-th adventurer in the team. Your task is to compute the product of all other adventurers' strengths for each adventurer, excluding their own strength.

# Input Format

# An integer n, which represents the number of adventurers in the team.
# n space separated integers, where each integer represents the strength of the i-th adventurer in the team.
# Constraints

# 2 <= strengths.length <= 10^5
# -30 <= strengths[i] <= 30
# The input is generated such that result[i] is guaranteed to fit in a 32-bit integer.
# Output Format

# Print an array result such that result[i] represents the product of all other adventurers' strengths, excluding the i-th adventurer.
# Sample Input 0

# 4
# 1 2 3 4
# Sample Output 0

# 24 12 8 6
# Sample Input 1

# 5
# -1 1 0 -3 3
# Sample Output 1

# 0 0 9 0 0
