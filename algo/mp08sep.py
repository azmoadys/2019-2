# link

data  = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

def solution(data):
    for i in range(0,len(data)):
        temp = [data[i]]
        for j in range (i+1, len(data)):
            temp.append(data[j])
            if sum(temp) == 0:
                print(temp)
        #print(temp)

if __name__ == '__main__':
    solution(data)
