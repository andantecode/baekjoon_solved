import sys

n = int(sys.stdin.readline())

plus = [0] * 1000001
minus = [0] * 1000001

for i in range(n):
    temp = int(sys.stdin.readline())
    if temp >= 0: plus[temp] = 1
    else: minus[-temp] = 1

num = -1000000

for item in minus[:0:-1]:
    if item == 1:
        print(num)
    num += 1

for item in plus:
    if item == 1:
        print(num)
    num += 1


