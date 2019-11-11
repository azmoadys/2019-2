import sys


def dfs(r,c):
    dp[r][c] += 1
    for d in direction:
        if 0<=r+d[0]<m and 0<=c+d[1]<n and travelmap[r][c] > travelmap[r+d[0]][c+d[1]]:
            dfs(r+d[0], c+d[1])


m, n = map(int, input().split())
travelmap = []
for i in range(m):
    travelmap.append(list(map(int, sys.stdin.readline().rstrip().split())))
dp = [[0 for i in range(n)] for j in range(m)]

direction = [[0,1], [0,-1], [1,0], [-1,0]]

dfs(0,0)

print(dp[m-1][n-1])
