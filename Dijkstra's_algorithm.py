def dijkstra(s,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0

    while True:
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True #d[v]を確定

        for j in range(n):
               d[j] = min(d[j],d[v]+cost[v][j]) #確定した頂点から移動できる頂点について、必要ならば距離を書き換える
    return d

################################
n,w = map(int,input().split()) #n:頂点数　w:辺の数

cost = [[float("inf") for i in range(n)] for i in range(n)]
#cost[u][v] : 辺uvのコスト(存在しないときはinf この場合は10**10)
for i in range(w):
    x,y,z = map(int,input().split())
    cost[x][y] = z
    cost[y][x] = z
print(dijkstra(0,n,w,cost))

#https://juppy.hatenablog.com/entry/2018/11/01/蟻本_python_単一最短経路法2（ダイクストラ法）_競技プ
