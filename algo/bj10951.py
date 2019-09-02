#https://www.acmicpc.net/problem/10951

import sys
while True:
	try:
		data1, data2 = map(int, sys.stdin.readline().split())
		print(data1+data2)
    except:
		break
