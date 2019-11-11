def sol(datas):
    cnt = 0
    result = []
    for data in datas:
        if data != 0:
            result.append(data)
        else:
            cnt +=1
    for i in range(cnt):
        result.append(0)
    print(result)


if __name__ == "__main__":
    sol([6, 0, 8, 2, 3, 0, 4, 0, 1])
