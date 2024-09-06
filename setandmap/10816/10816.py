import sys

input = sys.stdin.readline

n = int(input())
list_ = list(map(int, input().rstrip('\n').split(' ')))

dict_ = {}

for item in list_:
    if item in dict_.keys():
        dict_[item] += 1
    else:
        dict_[item] = 1


m = int(input())
key_list = list(map(int, input().rstrip('\n').split(' ')))

for key in key_list:
    print(dict_.get(key, 0), end=' ')
