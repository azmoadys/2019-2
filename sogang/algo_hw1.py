import sys

rows, columns = map(int, sys.stdin.readline().split())

mat = []
for i in range(rows):
    temp = sys.stdin.readline().split()
    for j in range(columns):
        temp[j] = int(temp[j])
    mat.append(temp)

# O(n^6)
#max_sum = 0
cnt= 0
for row_len in range(rows):
    for col_len in range(columns):
        for row in range(rows-row_len):
            for col in range(columns-col_len):
                temp = 0
                for row_num in range(row,row+row_len+1):
                    for col_num in range(col,col+col_len+1):
                        temp+=mat[row_num][col_num]
                if cnt == 0:
                    max_sum = temp
                    cnt+=1
                #print(row, row+row_len+1, col, col+col_len+1,temp, max_sum)
                if max_sum < temp:
                    max_sum = temp
                    max_col = [col,col+col_len]
                    max_row = [row,row+row_len]
# O(n^4)


# O(N^3)
