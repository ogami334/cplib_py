def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil,pi,factorial
    from operator import itemgetter
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    def SI(): return input().rstrip()
    def printns(x): print('\n'.join(x))
    inf = 10**17
    mod = 10**9 + 7
    #mod =998244353
#main code here!
    import heapq
    def dijkstra_heap(s):
        #始点sから各頂点への最短距離
        d = [float("inf")] * 100
        used = [True] * 100 #True:未確定
        d[s] = 0
        used[s] = False
        edgelist = []
        for e in edge[s]:
            heapq.heappush(edgelist,e)
        while len(edgelist):
            minedge = heapq.heappop(edgelist)
            #まだ使われてない頂点の中から最小の距離のものを探す
            if not used[minedge[1]]:
                continue
            v = minedge[1]
            d[v] = minedge[0]
            used[v] = False
            for e in edge[v]:
                if used[e[1]]:
                    heapq.heappush(edgelist,[e[0]+d[v],e[1]])
        return d

    ################################
    '''n,w = map(int,input().split()) #n:頂点数　w:辺の数

    edge = [[] for i in range(n)]
    #edge[i] : iから出る道の[重み,行先]の配列
    for i in range(w):
        x,y,z = map(int,input().split())
        edge[x].append([z,y])
        edge[y].append([z,x])
    print(dijkstra_heap(0))'''
    grid=[[0]*10 for i in range(10)]
    edge=[[] for i in range(100)]
    step=[[-1,0],[0,1],[0,-1],[1,0]]
    for i in range(10):
        s=SI()
        for j in range(10):
            if s[j]=="x":
                grid[i][j]=1
    #print(grid)
    for i in range(10):
        for j in range(10):
            for x,y in step:
                if 0<=i+x<10 and 0<=j+y<10:
                    if grid[i+x][j+y]==0 and grid[i][j]==0:
                        edge[10*i+j].append([0,10*(i+x)+y+j])
                    else:
                        edge[10*i+j].append([1,10*(i+x)+y+j])
    for i in range(10):
        for j in range(10):
            if grid[i][j]==0:
                lis=dijkstra_heap(10*i+j)
                break
        else:
            continue
        break
    #print(lis)
    for i in range(10):
        for j in range(10):
            if grid[i][j]==0:
                if lis[10*i+j]>2:
                    print("NO")
                    exit()
    print("YES")



if __name__=="__main__":
    main()
            
