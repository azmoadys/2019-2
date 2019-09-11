# https://www.acmicpc.net/problem/11365
# O(n^2)
import sys

def solution(data):
    answer =''
    length = len(data)-1
    for i in range(length, -1,-1):
        answer += data[i]
    return answer

if __name__ == '__main__':
    while True:
        data = sys.stdin.readline().rstrip()
        if data == 'END':
            break
        print(solution(data))
