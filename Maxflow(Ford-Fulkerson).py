from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())
N,E = inpl()
Start = 0
Goal = N-1
ans = 0
lines = defaultdict(set)
cost = [[0]*N for i in range(N)]
for i in range(E):
    a,b,c = inpl()
    if c != 0:
        lines[a].add(b)
        cost[a][b] += c
def Ford_Fulkerson(s): #sからFord-Fulkerson
    global lines
    global cost
    global ans
    queue = deque()     #BFS用のdeque
    queue.append([s,INF])
    ed = [True]*N    #到達済み
    ed[s] = False
    route = [0 for i in range(N)]   #ルート
    route[s] = -1
    #BFS
    while queue:
        s,flow = queue.pop()
        for t in lines[s]:  #s->t
            if ed[t]:
                flow = min(cost[s][t],flow)  #flow = min(直前のflow,line容量)
                route[t] = s
                queue.append([t,flow])
                ed[t] = False
                if t == Goal: #ゴール到達
                    ans += flow
                    break
        else:
            continue
        break
    else:
        return False
    #ラインの更新
    t = Goal
    s = route[t]
    while s != -1:
        #s->tのコスト減少，ゼロになるなら辺を削除
        cost[s][t] -= flow
        if cost[s][t] == 0:
            lines[s].remove(t)
        #t->s(逆順)のコスト増加，元がゼロなら辺を作成
        if cost[t][s] == 0:
            lines[t].add(s)
        cost[t][s] += flow
        t = s
        s = route[t]

    return True
while True:
    if Ford_Fulkerson(Start):
        continue
    else:
        break
print(ans)
