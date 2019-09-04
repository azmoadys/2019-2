# wrong!

import math

def average(num):
	return sum(num)/len(num)

case = int(input())
for i in range(case):
	temp = input()
	n,k = temp.split()
	n = int(n)
	k = int(k)
#	print(n,k)
	prices = list(map(int,input().split()))
#	print(sorted(prices))
	if max(prices)- min(prices) > 2*k:
		print("-1")
	else:
		avg = math.floor(average(prices))
		while avg-min(prices) < k:
			avg = avg+1
		print(avg)
