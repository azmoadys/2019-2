Input = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
total = []
length = len(Input)
dic = dict()
temp= 0
cnt = 0
for i in range(length):
    if i == length-1:
        if Input[i]!=0:
            temp += Input[i]
        total.append(temp)
        break
    if Input[i] != 0:
        temp += Input[i]
        if Input[i+1]==0:
            total.append(temp)
            temp = 0
        else:
            pass
    elif Input[i] ==0:
        total.append(0)
        dic[cnt] = i
        cnt +=1
    else:
        pass

length = len(total)
mx =0
cnt = 0
for i in range(length):
    if total[i] ==0:
        cnt+=1
    if i == 0:
        if total[0] == 0:
            mx = 1+total[1]
            mx_cnt = cnt-1
        else:
            continue
    elif i == length-1:
        if total[i] == 0:
            if total[i-1]+1 >mx:
                mx = total[i-1]+1
                mx_cnt = cnt-1
        else:
            break 
    else:
        pass
    
    if total[i] ==0:
        if total[i-1] + 1 + total[i+1] >mx:
            mx = total[i-1] + 1 + total[i+1]
            mx_cnt = cnt-1

print(dic[mx_cnt])

