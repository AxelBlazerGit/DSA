from os import *
from sys import *
from collections import *
from math import *

from typing import *

def minimumNet(n: int, k: int, fish: List[int]) -> int:
    # Write your code here.
    cur=len(fish)
    l=r=s=0
    while r<len(fish):
        s+=fish[r]
        r+=1
        while s>=k:
            cur=min(cur,r-l)
            s-=fish[l]
            l+=1
    return cur if sum(fish)>=k else -1
