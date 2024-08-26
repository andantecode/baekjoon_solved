import sys

num = int(input())
list_ = []

for i in range(num):
    temp = list(sys.stdin.readline().rstrip('\n').split(' '))
    temp = list(map(int, temp))
    list_.append(temp)

list_.sort(key=lambda x:(x[0], x[1]))

for items in list_:
    print(f'{items[0]} {items[1]}')

