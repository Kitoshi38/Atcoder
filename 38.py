def LCS(X, Y):
    LX = len(X)
    LY = len(Y)
    dp = [[0 for i in range(LX+1)] for j in range(LY+1)]
    for i in range(LY-1, -1, -1):
        for j in range(LX-1, -1, -1):
            r = max(dp[i+1][j], dp[i][j+1])
            if X[j] == Y[i]:
                r = max(r, dp[i+1][j+1]+1)
            dp[i][j] = r
    return dp[0][0]
    
    

q = int(input())

for i in range(q):
    X = input()
    Y = input()
    print(LCS(X, Y))
