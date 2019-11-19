import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
scores.sort(reverse = True)
sys.stdout.write(str(scores[0] - scores[-1]))
