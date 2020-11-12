def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,w = map(int,input().split()) #n:頂点数　w:辺の数

d = [[float("inf")]*n for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(w):
    x,y,z = map(int,input().split())
    x-=1
    y-=1
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
print(warshall_floyd(d))
#インデックスで与えられていることに注意
#ソース　https://juppy.hatenablog.com/entry/2018/11/01/蟻本_python_全点対最短経路法（ワーシャルフロイド法
