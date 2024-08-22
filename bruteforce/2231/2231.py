# 1000000까지의 분해합을 구하자...

list_ = list(range(1, 1000001))

def get_sum(x):
    sum_ = x
    while x > 0:
        sum_ += x % 10
        x //= 10
    
    return sum_

list_ = list(map(get_sum, list_))

target = int(input())
try:
    print(list_.index(target) + 1)
except:
    print(0)
