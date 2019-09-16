# https://www.acmicpc.net/problem/9020

import sys

def eratos(data):
    answer = []
    num = []
    for i in range(2,data):
        num.append(i)
    cnt = 2
    while True:
        try :
            num.remove(cnt*num[0])
            cnt +=1
        except :
            if num ==[]:
                break
            else:
                answer.append(num[0])
                num.remove(num[0])
    return answer
    
def solution(data, N):
    if N//2 in data:
        print(N//2)
        return N//2
    else:
        length = len(data)
        for i in range(length):
            if data[i] > N//2:
                strt = i-1
        for i in data[strt:]:
            if N-i in data:
                return i
            else:
                continue
    
if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for running in range(T):
        N = int(sys.stdin.readline().rstrip()) # target #
        result = solution(eratos(N),N)
        print(result)
        if result > N-result:
            print(N-result, result)
        else:
            print(result, N-result)
