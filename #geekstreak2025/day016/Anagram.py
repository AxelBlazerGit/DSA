#User function Template for python3


from collections import Counter
class Solution:
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        return Counter(s1)==Counter(s2)
