x = [1, 4, 7, 8, 10]
y = [2, 3, 9]
x_len = len(x)
y_len = len(y)

for j in range(y_len):
    for i in range(j,x_len):
        if x[i] >y[j]:
            temp = x[i]
            x[i] = y[j]
            y[j] = temp

y.sort()

print('X: ',x)
print("Y: ",y)
