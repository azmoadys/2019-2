# https://www.acmicpc.net/problem/1654

import sys

def solution(data,N):
    data.sort()
    maxi = 0
    len_cnt = dict()
    #for i in range(1,data[0]):
    i = 0
    while True:
        i+=1
        cnt =0
        length = data[0]//i
        for j in data:
            cnt+= j//length
        len_cnt[i] = length
        if cnt >= N:
            high = (len_cnt[i-1])
            low = (len_cnt[i])
            break
    while high >= low:
        mid = ((high+low)//2)
        cnt = 0
        for i in data:
            cnt += i//mid
        if cnt >= N:
            low = mid+1
            if maxi <mid:
                maxi = mid
        else:
            high = mid-1
    return maxi

if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().split())
    data = []
    for i in range(K):
        data.append(int(sys.stdin.readline().rstrip()))
    print(solution(data,N))
