# https://www.acmicpc.net/problem/9020

import sys


def eratos(data):
    answer = dict()
    checker = dict()
    deleted = dict()
    for i in range(2,data):
        checker[i] = False 
        deleted[i] = False
    cnt = 2
    strt = 2
    while True:
        if checker[strt] == True:
            strt+=1
            if strt >= data:
                break
            else:
                continue
        try:
            if checker[strt*cnt] ==True:
                cnt+=1
                continue
            checker[cnt*strt] = True
            cnt +=1
        except:
            answer[strt] = True
            checker[strt] = True
            cnt = 2
    return answer
 
def solution(data, N):
    if N//2 in data:
        return N//2
    else:
        temp = []
        for i in data:
            temp.append(i)
        length = len(temp)
        for i in range(length):
            if temp[i] > N//2:
                strt = i-1
                break
            else:
                continue
        for i in temp[strt::-1]:
            try:
                data[N-i]
                return i
            except:
                pass
    
if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for running in range(T):
        N = int(sys.stdin.readline().rstrip()) # target #
        eratos(N)
        result = solution(eratos(N),N)
        if result > N-result:
            print(N-result, result)
        else:
            print(result, N-result)
