import sys

n = int(input())

my_card = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))

my_card = {item: 1 for item in my_card}

print(my_card)

m = int(input())

validation_card = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))

for item in validation_card:
    try:
        print(my_card[item], end=' ')
    except:
        print(0, end=' ')

