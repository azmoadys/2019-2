import sys

num = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
for i in range(num):
    arr[i] = int(arr[i])
MAX = -10000
temp = 0
for i in range(num):
    temp += arr[i]
    if(MAX <temp):
        MAX = temp
    if(temp<0):
        temp = 0
print(MAX)
