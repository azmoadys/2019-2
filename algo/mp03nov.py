import sys
data = [2, 7, 9, 5, 1, 3, 5]

def sol(data):
    Min=data[0]
    result = (-1)*sys.maxsize
    for i in data:
        if result < i-Min:
            if i-Min>0:
                result = i-Min
            else:
                pass
        if i < Min:
            Min = i
    return result
if __name__=="__main__":
    print(sol(data))
