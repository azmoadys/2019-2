import sys

test_case = int(sys.stdin.readline())
dp = dict()
for _ in range(test_case):
    num = int(sys.stdin.readline())
    dp[1] = 1
    dp[2] = 2
    dp[3] =4
    for i in range(4,num+1):
        dp[i] = dp[i-1] + dp[i-2] +dp[i-3]
    print(dp[num])
            

