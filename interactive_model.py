#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial,sin
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7


n=I()
mx1=0
pos1=0
for i in range(1,n+1):
    if i==1:
        continue
    print("? {} {}".format(1, i),flush=True)
    dist = int(input().rstrip())
    if dist>mx1:
        mx1=dist
        pos1=i
mx2=0
for i in range(1,n+1):
    if i==pos1:
        continue
    print("? {} {}".format(pos1, i),flush=True)
    dist = int(input().rstrip())
    if dist>mx2:
        mx2=dist
print("! {}".format(mx2))
