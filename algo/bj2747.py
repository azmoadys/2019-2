memo = {1:1, 2:1}
def fibo(num):
	if num <  2:
		return num
	if num not in memo:
		memo[num] = fibo(num-1)+fibo(num-2)
	return memo[num]

import sys

data = sys.stdin.readline().split()
print(fibo(int(data[0])))
