X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
Y = [1, 8, 9, 10, 15]
cnt =0
for i in range(len(X)):
    if X[i] == 0:
        X[i] = Y[cnt]
        cnt+=1
    else:
        continue

X.sort()
print(X) 
