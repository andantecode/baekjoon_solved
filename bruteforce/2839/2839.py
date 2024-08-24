
N = int(input())

def solve(num: int):
    list_ = []
    count_5kg = 0

    while num >= 0:
        if num % 3 == 0:
            list_.append(int(num / 3 + count_5kg))
        count_5kg += 1
        num -= 5

        
    return min(list_) if len(list_) != 0 else -1

print(solve(N))