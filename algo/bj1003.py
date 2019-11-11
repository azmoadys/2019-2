import sys

T = int(sys.stdin.readline())
nums = []
for _ in range(T):
    nums.append(int(sys.stdin.readline()))
dp = {0:[1,0],1:[0,1]}
MAX = max(nums)
for i in range(2,MAX+1):
    temp = []
    temp.append(dp[i-2][0]+dp[i-1][0])
    temp.append(dp[i-2][1]+dp[i-1][1])
    dp[i] = temp
for num in nums:
    print(dp[num][0],dp[num][1])

