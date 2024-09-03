import sys

input = sys.stdin.readline

people = set()

n = int(input())

for i in range(n):
    name, status = input().rstrip('\n').split(' ')

    if status == 'enter':
        people.add(name)
    elif status == 'leave':
        people.remove(name)
    
people = list(people)
people.sort(reverse=True)

for person in people:
    print(person)
    


