# https://www.acmicpc.net/problem/2960
# O(n^2)

import sys

def solution(N,K):
    total = []
    for i in range(2,N+1):
        total.append(i)
    cnt = 1
    while True:
        i = total[0]
        temp = []

        for j in total:
            if j-j//i*i == 0:
                temp.append(j)
        for j in temp:
            #print(cnt, j, total)
            total.remove(j)
            if cnt == K:
                return j
            cnt += 1

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    print(solution(N,K))
