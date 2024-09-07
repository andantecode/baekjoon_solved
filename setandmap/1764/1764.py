import sys

input = sys.stdin.readline

n, m = list((map(int, input().rstrip('\n').split(' '))))

no_listen = {}
no_listenseen = []

for i in range(n):
    tmp = input().rstrip('\n')
    no_listen[tmp] = 1

for i in range(m):
    tmp = input().rstrip('\n')
    if tmp in no_listen.keys():
        no_listenseen.append(tmp)

no_listenseen.sort()

print(len(no_listenseen))

for item in no_listenseen:
    print(item)
