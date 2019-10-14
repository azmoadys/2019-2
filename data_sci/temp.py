maps = ["1,2,3,4","5,6,7,8"]
dic = dict()
row  = len(maps)
col = []
for row in maps:
    cnt =0
    for cntry in row:
        print(cntry)
        cnt+=1
    print(cnt)
    col.append(cnt)


print(row)
print(col)
