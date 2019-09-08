# https://www.acmicpc.net/problem/2490

import sys

def solution():
    sum_data = 0
    data = sys.stdin.readline().split()
    for i in data:
        sum_data += int(i)
    if sum_data == 1:
        return 'C'
    elif sum_data == 2:
        return 'B'
    elif sum_data == 3:
        return 'A'
    elif sum_data == 4:
        return 'E'
    else:
        return 'D'

if __name__ == '__main__':
    for i in range(0,3):
        print(solution())
