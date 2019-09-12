# https://www.acmicpc.net/problem/11586
# O(n^2)
import sys
matrix = []
N = int(input())
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    matrix.append(temp)
emo = int(input())

if emo == 3:
    for i in range(N):
        print(matrix[N-1-i])
elif emo == 2:
    for i in range(N):
        for j in range(N):
            sys.stdout.write(matrix[i][N-1-j])
        sys.stdout.write('\n')
elif emo == 1:
    for i in range(N):
        print(matrix[i])
else:
    pass
