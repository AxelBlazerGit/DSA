n=int(input())
arr=list(map(int, input().split()))
def f(n,arr):
    s=sum(arr)
    l=0
    for i in range(n):
        if l==s-l-arr[i]:
            print(i)
            return
        l+=arr[i]
    print(-1)
f(n,arr)
# Long ago, in the mythical land of Numetron, a magical sequence of energy shards was discovered, said to hold the key to restoring peace and prosperity to the realm. The legend tells of a special shard hidden in the sequence—a shard that perfectly divides the energy flow of the others.

# This shard is special because it is positioned in such a way that the total energy of all shards on its left is exactly equal to the total energy of all shards on its right. Finding this shard is the key to unlocking the ancient power stored within the sequence.

# Your Mission:-

# As the chosen adventurer, your task is to write a spell—code—that will help locate this special shard. The Oracle has warned that the sequence may not always contain such a shard, and in such cases, you must return empty-handed to avoid a false prophecy.

# Rules of the Quest:-

# 1.You are given an ancient sequence of energy shards, each represented as an integer. These numbers can be positive, negative, or zero, reflecting their unique energy properties.

# 2.You must determine the position of the special shard that divides the sequence into two equal-energy parts. If no such shard exists, report that the quest cannot be fulfilled and return -1.

# 3.If there are multiple special shards, then return the index of the first occurring special shard.

# Input Format

# An integer n — the number of energy shards in the sequence.
# n space separated integers, where each element represents the energy of a shard.
# Constraints

# The sequence length can range from 3 to 100,000 shards.
# Each shard’s energy level lies between -10,000 and 10,000.
# Output Format

# A single integer — the 1-based index of the first special shard. If no such shard exists, return -1.
# Sample Input 0

# 4
# 1 2 0 3
# Sample Output 0

# 2
# Explanation 0

# The sum of energies to the left (1 + 2) is equal to the sum of energies to the right (3).

# Sample Input 1

# 4
# 1 1 1 1
# Sample Output 1

# -1
# Explanation 1

# There is no shard that divides the sequence into two equal-energy parts.

# Sample Input 2

# 7
# -7 1 5 2 -4 3 0
# Sample Output 2

# 3
# Explanation 2

# The sum of energies to the left (-7 + 1 + 5 = -1) is equal to the sum of energies to the right (-4 + 3 + 0 = -1).
