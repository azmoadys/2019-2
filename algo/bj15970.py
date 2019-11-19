import sys

N = int(sys.stdin.readline())
dots = dict()
for _ in range(N):
    pos, clr = map(int,sys.stdin.readline().split())
    dots[pos] = clr
clr = dict()

for key in dots:
    try:
        clr[dots[key]].append(key)
        clr[dots[key]].sort()
    except:
        clr[dots[key]] = [key]
cnt = 0
for color in clr.values():
    LEN = len(color)
    for i in range(LEN):
        if i == 0:
            cnt += color[i+1] - color[i]
        elif i == LEN-1:
            cnt += color[i] - color[i-1]
        else:
            if color[i]-color[i-1] > color[i+1] - color[i]:
                cnt += color[i+1] - color[i]
            else:
                cnt += color[i] - color[i-1]

sys.stdout.write(str(cnt))
