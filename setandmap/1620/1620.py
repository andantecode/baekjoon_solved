import sys

input = sys.stdin.readline

n, m = map(int, (input().rstrip('\n').split(' ')))
dict_intkey = {}
dict_namekey = {}

for i in range(n):
    poketmon_name = input().rstrip('\n')
    dict_intkey[i+1] = poketmon_name
    dict_namekey[poketmon_name] = i+1


for j in range(m):
    command = input().rstrip('\n')
    
    try:
        command = int(command)
        print(dict_intkey[command])
    except:
        print(dict_namekey[command])
