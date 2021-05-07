def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    import decimal
    from decimal import Decimal
    from collections import Counter, deque
    from collections import defaultdict
    from itertools import combinations,permutations, groupby, product,accumulate
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil,pi,factorial,sqrt
    from operator import itemgetter
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    def SI(): return input().rstrip()
    def FMI(): return map(float,input().split())#64bit 
    #def FLI(): return list(map(float,input().split()))#64bit 
    def DECMI(): return map(Decimal, input().split())
    #def DECLI(): return list(map(Decimal, input().split())) 
    def printns(x): print('\n'.join(x))
    inf = 10**17
    mod = 10**9 + 7
    #mod =998244353
#main code here!
    X,Y,R = DECMI()
    xmax = floor(X+R)
    xmin = ceil(X-R)
    ans = 0
    for x in range(xmin,xmax+1):
        ywidth = (R**2 - (x-X)**2).sqrt()
        ymax_tmp = floor(Y + ywidth)
        ymin_tmp = ceil(Y - ywidth)
        ans += ymax_tmp - ymin_tmp + 1
    print(ans)

if __name__=="__main__":
    main()