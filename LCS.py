X = ""
Y = ""
dp = [[0 for i in range(len(X)+1)] for j in range(len(Y)+1)] #0で初期化

for i in range(len(Y)):
    for j in range(len(X)):
        if X[j] == Y[i]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
