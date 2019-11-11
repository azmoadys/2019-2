import sys

floor = int(sys.stdin.readline())
val = []
for _ in range(floor):
    val.append(int(sys.stdin.readline()))
dp = [val[0], val[1]+val[0]]
for _ in range(floor-2):
    dp.append(0)
dp[2] = max(val[0], val[1])+val[2]
for i in range(3,floor):
    dp[i] = max(dp[i-2],val[i-1]+dp[i-3])+val[i]
print(dp[floor-1])
