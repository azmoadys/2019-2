import random

def sol(data):
    result = []
    LEN = len(data)
    print(random.sample(data,LEN))

if __name__ == "__main__":
    sol([1, 2, 3, 4, 5, 6])
