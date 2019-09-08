#  https://www.acmicpc.net/problem/2702

import sys

def gcd(num1, num2):
    temp = num1 - num2
    if num2 == 0:
        result =  num1
    else :
        result = gcd(max(num2, temp), min(num2, temp))
    return result

def lcm(n1, n2, g_n):
    return int(n2*(n1/g_n))

def solution():
    n1, n2 = map(int, sys.stdin.readline().split())
    g_n = gcd(max(n1, n2), min(n1, n2))
    print(lcm(n1, n2, g_n), g_n)

if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        solution()


