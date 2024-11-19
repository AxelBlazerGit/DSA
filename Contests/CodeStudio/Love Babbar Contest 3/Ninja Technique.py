from os import *
from sys import *
from collections import *
from math import *

from typing import *

def ninjaTechnique(n: int, a: List[List[int]])-> int:
    
    # Write your Code Here
    # pass
    a = [(min(start, end), max(start, end)) for start, end in a]
    a.sort(key=lambda x: x[1])
    ans=[]
    count = 0
    ninja = -float('inf')

    for start, end in a:
        if ninja < start:
            count += 1
            ninja = end

    ans.append(count)

    return ans[0]
