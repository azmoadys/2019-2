Input = [0, -3, 5, -4, -2, 3, 1, 0]

length = len(Input)
answer = []
total = sum(Input)
f_sum=0
for i in range(length):
    if i ==0:
        if total-Input[i] == 0 :
            answer.append(i)
        else:
            total -= Input[i]
            f_sum += Input[i]
            continue
    else:
        total -= Input[i]
        if f_sum == total:
            answer.append(i)
        else:
            pass
        f_sum += Input[i]
print(answer) 
