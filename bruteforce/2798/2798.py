# N장의 카드가 주어졌을 때 3장을 선택해 뽑아 더해서
# M과 가장 가깝게 만들어야함

N, M = list(map(int, input().split(" ")))
list_ = list(map(int, input().split(" ")))

list_.sort()
result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_ = list_[i] + list_[j] + list_[k]
            if sum_ <= M and result < sum_:
                result = sum_
            else: break

print(result)

