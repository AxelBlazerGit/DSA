import sys
sys.set_int_max_str_digits(10**5)
#User function Template for python3

class Solution:
    def roundToNearest (self, s) : 
        #Complete the function
        start = 0
        for i in s:
            if i != '0':
                break
            start += 1
        
        s = str(int(s))
        
        if s[-1] == '0':
            return ('0' * start) + s
        
        if s[-1] < '6':
            result = s[:-1] + '0'
            return ('0' * start) + result
        s = int(s)
        s = (s // 10) * 10
        s += 10
        return ('0' * start) + str(s)
