from os import *
from sys import *
from collections import *
from math import *

from typing import *

def makeItEqual(a: int, b: int, c: int)-> int:

    # Write your Code here
    # pass
    # 010
    # 011
    # 101
    # ---
    # 211
    # if both are 0/1 and c bit is 1/0=>add 2
    # if both are 1   and c bit is 0=>add 1
    # if c bit is set and one is unset => add 1
    # 15 9 6
    # a= 1 1 1 1
    # b= 1 0 0 1
    # c= 0 1 1 0
    # ------------
    #    1 1 1 1

    c=bin(c)[2:]
    a=bin(a)[2:]
    b=bin(b)[2:]
    l=max(len(a),len(b),len(c))
    a=a.zfill(l)[::-1]
    b=b.zfill(l)[::-1]
    c=c.zfill(l)[::-1]
    moves=0
    for x in range(len(c)):
        if c[x]=='1':
            if a[x]=='0':
                moves+=1
            if b[x]=='0':
                moves+=1
        if c[x]=='0':
            if a[x]==b[x] and a[x]=='1':
                moves+=1
    return moves
