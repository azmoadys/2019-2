def sol(datas):
    dic = dict()
    LEN = len(datas)
    temp_datas = set(datas)
    for data in temp_datas:
        dic[data] = 0
    for data in datas:
        dic[data]+=1
    for key in dic:
        if dic[key] > LEN//2:
            print(key)

if __name__ == "__main__":
    sol([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2])
