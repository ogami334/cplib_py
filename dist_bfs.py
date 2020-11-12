import sys
input = sys.stdin.readline

N,u,v=map(int,input().split())
E=[tuple(map(int,input().split())) for i in range(N-1)]

EDGE=[[] for i in range(N+1)]

for x,y in E:
    EDGE[x].append(y)
    EDGE[y].append(x)

from collections import deque
T=[-1]*(N+1)

Q=deque()
Q.append(u)
T[u]=0

while Q:
    x=Q.pop()
    for to in EDGE[x]:
        if T[to]==-1:
            T[to]=T[x]+1
            Q.append(to)
print(T)
#未探索、探索済みのステータスを距離とともに一つにまとめているのが上手
#探索済みか否かをまとめておくのが大切か。
