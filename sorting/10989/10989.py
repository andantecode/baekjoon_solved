# 수 정렬하기 -- 1~10000까지의 자연수 중복 허용 (오름차순)

import sys

n = int(sys.stdin.readline())

plus = [0] * 10001

for i in range(n):
    temp = int(sys.stdin.readline())
    plus[temp] += 1
    
num = 0

for item in plus:
    if item != 0:
        for j in range(item):
            print(num)
    num += 1


