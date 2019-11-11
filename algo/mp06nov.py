import sys

def sol(data):
    MAX = 0
    temp = 0
    temp_list = []
    MAX_list = []
    for i in data:
        temp += i
        temp_list.append(i)
        if temp > MAX:
            MAX = temp
            MAX_list = temp_list
        if temp <0:
            temp = 0
            temp_list = []
    if MAX == 0:
        MAX_list.append(max(data))
        MAX = max(data)
    print(MAX, MAX_list)
if __name__ =="__main__":
    sol([-2, 1, -3, 4, -1, 2, 1, -5, -4])
    sol([-8, -3, -6, -2, -5, -4])
