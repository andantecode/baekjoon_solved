import sys

num = list(sys.stdin.readline().rstrip('\n'))

num.sort(reverse=True)

for item in num:
    print(item, end='')
