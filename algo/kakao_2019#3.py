key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def solution(key, lock):
    answer = True
    lock_loc = []
    row_cnt = 0
    for row in lock:
        col_cnt = 0
        for column in row:
            if column == 0:
                lock_loc.append([row_cnt,col_cnt])
            col_cnt+=1
        row_cnt+=1
    print(lock_loc)
    return answer


if __name__ == '__main__':
    print(solution(key, lock))
