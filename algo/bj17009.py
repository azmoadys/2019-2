#https://www.acmicpc.net/problem/17009

import sys

def solution():
    sum_a = 0
    sum_b = 0
    for i in range(3,0,-1):
        sum_a += i*int(input()) 
    for i in range(3,0,-1):
        sum_b += i*int(input())
    if sum_a >sum_b:
        print('A')
    elif sum_a<sum_b:
        print('B')
    else:
        print('T')

if __name__ == "__main__":
    solution()
