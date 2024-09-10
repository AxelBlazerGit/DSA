#User function Template for python3

from collections import defaultdict

class Solution:
    
    def connection(self, point, chains, checked):
        checked[point] = 1
        for next_point in chains[point]:
            if not checked[next_point]:
                self.connection(next_point, chains, checked)

    def isCircle(self, arr):
        freq = defaultdict(int)
        chains = defaultdict(list)
        for string in arr:
            start = ord(string[0]) - ord('a')
            end = ord(string[-1]) - ord('a')
            freq[start] += 1
            freq[end] -= 1
            chains[start].append(end)

        if any(count != 0 for count in freq.values()):
            return 0
    
        checked = [0] * 26
        start_char = ord(arr[0][0]) - ord('a')
        self.connection(start_char, chains, checked)
        
        for char in freq:
            if not checked[char]:
                return 0
        
        return 1
