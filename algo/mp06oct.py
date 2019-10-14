Input = [-10, -3, 5, 6, -2]
pos = []
neg = []
for i in Input:
    if i >=0:
        pos.append(i)
    else:
        neg.append(i)

pos.sort()
neg.sort()

if pos[0]*pos[1] >= neg[0]*neg[1]:
    print(pos[0], pos[1])
else:
    print(neg[0], neg[1])
