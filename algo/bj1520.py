import sys

row, col = map(int, sys.stdin.readline().split())
value = []

for i in range(row):
    value.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1]*col for _ in range(row)]
dp[0][0] = 1

def path(i,j):
    if dp[i][j] > -1:
        return dp[i][j]
    dp[i][j] = 0  
    if j > 0 and value[i][j] < value[i][j-1]: # right
        dp[i][j] += path(i,j-1)
    if i > 0 and value[i][j] < value[i-1][j]: # down
        dp[i][j] += path(i-1,j)
    if j+1< col and value[i][j+1] > value[i][j]: # left
        dp[i][j] += path(i,j+1)
    if i+1 < row and value[i+1][j] > value[i][j]:
        dp[i][j] += path(i+1,j)
    return dp[i][j]

for i in range(row):
    for j in range(col):      
        path(i,j)    
print(dp[row-1][col-1])
