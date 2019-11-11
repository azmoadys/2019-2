def sol(data):
    zero = []
    one = []
    two = []
    for _ in data:
        if _ == 0:
            zero.append(_)
        elif _ == 1:
            one.append(_)
        else:
            two.append(_)
    result = zero + one + two
    return result
if __name__ == "__main__":
    print(sol([0, 1, 2, 2, 0, 0, 0, 1]))
