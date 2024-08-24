
M, N = map(int, input().split(' '))

matrix = []

for i in range(M):
    temp_list = list(input())
    matrix.append(temp_list)

def count_number(matrix, start_row, start_col):
    case_1, case_2 = 0, 0
    start_w = 'WB'*25
    start_b = 'BW'*25

    for i in range(start_row, start_row+8, 2):
        for j in range(start_col, start_col+8):
            if matrix[i][j] != start_w[j]: case_1 += 1
            if matrix[i][j] != start_b[j]: case_2 += 1
    for i in range(start_row+1, start_row+8, 2):
        for j in range(start_col, start_col+8):
            if matrix[i][j] != start_b[j]: case_1 += 1
            if matrix[i][j] != start_w[j]: case_2 += 1

    return case_1 if case_1 < case_2 else case_2

count=64

for i in range(M-8+1):
    for j in range(N-8+1):
        temp_count = count_number(matrix, i, j)
        if temp_count < count:
            count = temp_count

print(count)
