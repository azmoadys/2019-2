import sys
num = int(sys.stdin.readline())
value = [[0]*3 for _ in range(num)]
for i in range(num):
    value[i][0],value[i][1],value[i][2] = map(int, sys.stdin.readline().split())

dp = [[0]*3 for _ in range(num)]
dp[0] = value[0]

for i in range(1,num):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+value[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+value[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+value[i][2]
print(min(dp[num-1]))
