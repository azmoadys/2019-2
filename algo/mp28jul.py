import sys
def sol(data):
    data.sort()
    prev = data[0]
    for i in range(1,len(data)):
        if prev == data[i] and data[i] != data[i+1]:
            sys.stdout.write(str(data[i])+" ")
        else:
            prev = data[i]
    sys.stdout.write("\n")
if __name__ == "__main__":
    sol([0, 6, 3, 4, 0])
    sol([5, 4, 3, 2, 1, 1, 1, 1, 1, 2])
