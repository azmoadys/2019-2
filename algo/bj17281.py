import sys

def baseball(hit,base, score,out,inning):
    if hit == 1:
        if base[3] == 1:
            score+=1
        for _ in range(3,1,-1):
            base[_] = base[_-1]
        base[0] = 1
    elif hit == 2:
        if base[3] == 1:
            score+=1
        if base[2] == 1:
            score+=1
        for _ in range(3,2,-1):
            base[_] = base[_-2]
        base[0] = 1
        base[1] = 0
    elif hit == 3:
        if base[3] == 1:
            score+=1
        if base[2] == 1:
            score+=1
        if base[1] == 1:
            score+=1
        base[3] = 1
        for _ in range(3):
            base[_] = 0
    elif hit == 4:
        for _ in range(4):
            if base[_] == 1:
                score+=1
            base[_] = 0
        score+=1
    else:
        out[0] +=1
        if out[0]==3:
            out[0] = 0
            inning[0]+=1
        for _ in range(4):
            base[_] = 0
    return score

base = [0 for _ in range(4)]
score = 0
out = [0]

cnt = 0
inning = [1]
LEN = int(sys.stdin.readline())
status = []
for i in range(LEN):
    status.append(list(map(int,sys.stdin.readline().split())))
print(status)
selected = dict()
for _ in range(9):
    seleceted[_] = False
selected[3] = True

for a in range(1,8):
    score = 0
    selected[a] = True
    for b in range(1,8)
        if selected[b] == True:
            continue



while inning[0] <= LEN:
    score = baseball()
    cnt +=1
    if cnt == 8:
        cnt = 0

print(score)
print(base)
