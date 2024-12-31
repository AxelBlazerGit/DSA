#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        hash={}
        for i in arr:
            k=tuple(sorted(i))
            if k in hash:
                hash[k].append(i)
            else:
                hash[k]=[i]
        return list(hash.values())
