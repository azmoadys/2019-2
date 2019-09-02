#https://www.acmicpc.net/problem/2480

import sys

data = sys.stdin.readline().split() #data = list

for i in range(len(data)):
	data[i] = int(data[i]) #change string to int

if data[0] == data[1] and data[1]==data[2]:
	print(10000+(data[0]*1000))
elif data[0] == data[1] and data[1] != data[2]:
	print(1000 +(data[0]*100))
elif data[0] != data[1] and data[1] == data[2]:
	print(1000 +(data[1]*100))
elif data[0] == data[2] and data[1] != data[2]:
	print(1000 +(data[0]*100))
else:
	print(max(data)*100)


