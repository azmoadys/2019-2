# O(n^2)

data1 = [4, 2, -3, -1, 0, 4]
data2 = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

def solution(data):
    length = len(data)
    for i in range(length):
        result = data[i]
        for j in range(i,length):
            if i != j:
                result += data[j]
            if result == 0:
                print(data[i:j+1])

if __name__ == "__main__":
    solution(data1)
    solution(data2)
