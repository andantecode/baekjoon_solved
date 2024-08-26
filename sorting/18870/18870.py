import sys

num = int(sys.stdin.readline())
list_ = list(map(int, list(sys.stdin.readline().rstrip('\n').split(' '))))

sorted_list = sorted(set(list_))

index = 0
dict_ = {sorted_list[i]: i for i in range(len(sorted_list))}

for item in list_:
    print(dict_[item], end=' ')
            

