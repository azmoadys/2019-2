# https://www.acmicpc.net/problem/2750

import sys

def bubble_sort(data):
    length = len(data)

    for i in range(length-1):
        #print(data)
        for j in range(length-i-1):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    answer = data
    return answer

def selection_sort(data):
    length = len(data)
    for i in range(length):
        data[i] = min(data[i:])
    answer = data
    return answer


if __name__ == '__main__':
    data = []
    for i in range(int(input())):
        data.append(int(input()))
    #print('bubble sort : ', bubble_sort(data))
    #print('selection sort : ', selection_sort(data))
    
    for i in bubble_sort(data):
        print(i)
