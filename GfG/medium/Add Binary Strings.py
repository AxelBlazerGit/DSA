#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
    n1,n2=len(s1),len(s2)
    max_len = max(n1, n2)
    s1 = s1.zfill(max_len)
    s2 = s2.zfill(max_len)
    add=list()
    carry=0
    for i in range(max_len):
        check=int(s1[max_len-i-1])+int(s2[max_len-i-1])+carry
        add.append(0 if check % 2 == 0 else 1)
        carry=1 if check>1 else 0
        
    if carry:
        add.append(1)
        
    result = "".join(map(str, add[::-1])).lstrip('0')
    
    return result if result else "0"
