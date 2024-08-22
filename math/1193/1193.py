# 분수 찾기
# 1. 1행 기준으로 대각선으로 읽어감 (i=홀수)
# 2. 1열 기준으로 대각선으로 읽어감 (i=짝수)
# 1행 기준으로만 대각선으로 읽어간다고 생각하면 1행의 값들은 1, 2, 4, 7, 11, 16, ...
# 각 잔차가 1, 2, 3, 4, 5, ...
# target을 입력받아 해당 값을 세기 직전의 1행의 값 + k로 나타낼 수 있음
# 해당 열이 짝수일 경우
# 1행의 열을 col로 나타내면 (1, col) 기준으로 (1+k, col-k)로 나타낼 수 있음
# 해당 열이 홀수일 경우
# 1열의 행을 row로 나타내면 (row, 1) 기준으로 (row-k, 1+row)로 나타낼 수 있음


maximum_x = 100000000
list_ = [1, ]
step = 1

target = int(input())

for i in range(maximum_x):
    list_.append(list_[-1] + step)
    step += 1

    if target - list_[-1] < 0:
        break

k = target - list_[-2]
index = len(list_[:-1])

print(list_)
print(f'k = {k}, index = {index}')

if index % 2 == 0:
    print(f'{1 + k}/{index - k}')
else:
    print(f'{index - k}/{1 + k}')


