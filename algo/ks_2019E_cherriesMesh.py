# problem URL
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/0000000000170721
# 4th Sep

def selection():
    n,m = map(int, sys.stdin.readline().split())
    result = n+m
    return str(result)

import sys

test_case = int(input())

for i in range(test_case):
     sys.stdout.write(selection())
