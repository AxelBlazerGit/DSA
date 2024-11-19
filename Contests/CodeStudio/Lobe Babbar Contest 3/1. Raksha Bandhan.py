from os import *
from sys import *
from collections import *
from math import *

from typing import *

def rakshaBandhan(arr: List[int], n: int)-> int:

    # Write your Code here
    pos=[x for x in arr if x>=0]
    neg=sorted([x for x in arr if x<0])
    neg.reverse()
    ans=len(pos)
    cur=sum(pos)
    if not cur: return 0
    for i in neg:
        if cur+i>0:
            cur+=i
            ans+=1
    return ans
